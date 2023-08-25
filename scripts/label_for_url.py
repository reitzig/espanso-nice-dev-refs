#!/usr/bin/env python3

import re
import sys
from urllib.parse import unquote


# TODO: refactor into loop over (regexp, lambda)
# TODO: make the list extendable -- how?
#       use case: AOK Systems Dev Handbook


def prettify(anchor_arg: str) -> str:
    a, _ = re.subn(r"(?:^|[-+\s]+)([a-zA-Z])", lambda m: f" {m[1]}".upper(), unquote(anchor_arg))
    return a.strip()


# TODO: Python >=3.9: Remove and replace usages with removeprefix
# From: https://stackoverflow.com/q/16891340/539599
def remove_prefix(text: str, prefix: str) -> str:
    if text.startswith(prefix):
        return text[len(prefix) :]
    return text


def determine_label(input_url: str) -> str:
    if m := re.search(
        r"^https://[^/]*bitbucket[^/]*/(?:projects|users)/(?P<project>[^/]+)/repos/(?P<repo>[^/]+)/"
        r"pull-requests/(?P<pr>\d+)/?"
        r"(commits/(?P<commit>[a-fA-F0-9]+))?"
        r"(overview\?commentId=(?P<comment>\d+))?"
        r"((diff)?#(?P<file>[^?]+)(\?[tf]=(?P<line>[0-9,-]+))?)?",
        input_url,
    ):
        pr = f"#{m.group('pr')}" if m.group("pr") else ""
        filename = f":{unquote(m.group('file'))}" if m.group("file") else ""
        line = f"#{m.group('line')}" if m.group("line") else ""
        comment = f".{m.group('comment')}" if m.group("comment") else ""
        commit = f"@{m.group('commit')[0:8]}" if m.group("commit") else ""
        return f"{m.group('project')}/{m.group('repo')}{pr}{commit}{filename}{line}{comment}"
    elif m := re.search(
        r"^https://[^/]*bitbucket[^/]*/(?:projects|users)/(?P<project>[^/]+)/repos/(?P<repo>[^/]+)/"
        r"commits(/(?P<commit>[a-fA-F0-9]+))?/?"
        r"(#(?P<file>[^?]+))?"
        r"(\?until=(?P<branch>[^&]+))?",
        input_url,
    ):
        commit = f"@{m.group('commit')[0:8]}" if m.group("commit") else ""
        branch = f"@{unquote(m.group('branch'))}" if m.group("branch") else ""
        filename = f":{unquote(m.group('file'))}" if m.group("file") else ""
        return f"{m.group('project')}/{m.group('repo')}{commit}{branch}{filename}"
    elif m := re.search(
        r"^https://[^/]*bitbucket[^/]*/(?:projects|users)/(?P<project>[^/]+)/repos/(?P<repo>[^/]+)/"
        r"compare/(commits|diff)\?"
        r"(?:targetBranch=(refs%2Fheads%2F(?P<target_branch>[^&]+)|(?P<target_commit>[a-f0-9]+)&))?"
        r"sourceBranch=(refs%2Fheads%2F(?P<source_branch>[^&]+)|(?P<source_commit>[a-f0-9]+))",
        input_url,
    ):
        source_branch = unquote(m.group("source_branch")) if m.group("source_branch") else ""
        source_commit = m.group("source_commit")[0:8] if m.group("source_commit") else ""
        source = f"{source_branch}{source_commit}"
        target_branch = unquote(m.group("target_branch")) if m.group("target_branch") else ""
        target_commit = m.group("target_commit")[0:8] if m.group("target_commit") else ""
        target = f"{target_branch}{target_commit}"
        if target == "":
            return f"{m.group('project')}/{m.group('repo')}@{source}"
        else:
            return f"{m.group('project')}/{m.group('repo')} {source}⭤{target}"
    elif m := re.search(
        r"^https://[^/]*bitbucket[^/]*/(?:projects|users)/(?P<project>[^/]+)"
        r"(/repos/(?P<repo>[^/]+))?"
        r"(/(?:browse|diff)(/(?P<file>[^#?]+))?)?"
        r"(\?at=refs%2Fheads%2F(?P<branch>[^&#]+))?"
        r"(\?until=(?P<commit>[a-fA-F0-9]+))?"
        r"(#(?P<line>[0-9,-]+))?",
        input_url,
    ):
        repo = f"/{m.group('repo')}" if m.group("repo") else ""
        branch = f"@{unquote(m.group('branch'))}" if m.group("branch") else ""
        commit = f"@{m.group('commit')[0:8]}" if m.group("commit") else ""
        filename = f":{unquote(m.group('file'))}" if m.group("file") else ""
        line = f"#{m.group('line')}" if m.group("line") else ""
        return f"{m.group('project')}{repo}{branch}{commit}{filename}{line}"
    elif m := re.search(
        r"^https://[^/]*jira[^/]*/browse/(?P<project>\w+)(-(?P<issue>\d+))?"
        r"(?:\?focusedCommentId=(?P<comment>\d+))?",
        input_url,
    ):
        project = m.group("project")
        issue = f"-{m.group('issue')}" if m.group("issue") else ""
        comment = f".{m.group('comment')}" if m.group("comment") else ""
        return f"{project}{issue}{comment}"
    elif m := re.search(
        r"^https://gist.github.com/(?P<account>[^/]+)/"
        r"(?P<uid>[a-f0-9]+)(?:#file-(?P<fileline>[^?]+))?$",
        input_url,
    ):
        # Take apart the wicked file-line format:
        fileline_parts = m.group("fileline").split("-") if m.group("fileline") else None
        filename_parts, line_part = (
            [fileline_parts[0:-1], fileline_parts[-1]]
            if fileline_parts and re.search(r"^L\d+$", fileline_parts[-1])
            else [fileline_parts, ""]
        )

        filename = f":{'-'.join(filename_parts)}" if fileline_parts else ""
        line = f"#{line_part.replace('L', '')}" if line_part else ""
        return f"{m.group('account')}/{m.group('uid')[0:6]}{filename}{line}"
    elif m := re.search(
        r"https://[^/]*git(hub|lab)[^/]*/(?P<project>[^/]+)/(?P<repo>[^/#]+)/?"
        r"(?:wiki/(?P<wiki_page>[^/#?]+))?"
        r"(?:#(?P<anchor>[a-z][a-zA-Z0-9_-]+))?"
        r"$",
        input_url,
    ):  # NB: Include $ to not prematurely match any of the next two cases
        wiki_page = f" > {prettify(m.group('wiki_page'))}" if m.group("wiki_page") else ""
        anchor = f" > {prettify(m.group('anchor'))}" if m.group("anchor") else ""
        return f"{m.group('project')}/{m.group('repo')}{wiki_page}{anchor}"
    elif m := re.search(
        r"^https://[^/]*git(hub|lab)[^/]*/(?P<project>[^/]+)/(?P<repo>[^/]+)(/-)?/("
        r"((issues|pull|discussions|merge_requests)/(?P<number>\d+)"
        r"(#(issue|discussion)comment-(?P<comment_id>\d+))?)"
        r"|(releases/tag/(?P<release_tag>[^/#?]+))"
        r")",
        input_url,
    ):
        number = f"#{m.group('number')}" if m.group("number") else ""
        comment_id = f".{m.group('comment_id')}" if m.group("comment_id") else ""
        release_tag = f"@{m.group('release_tag')}" if m.group("release_tag") else ""
        return f"{m.group('project')}/{m.group('repo')}{number}{comment_id}{release_tag}"
    elif m := re.search(
        r"^https://[^/]*git(hub|lab)[^/]*/(?P<project>[^/]+)/(?P<repo>[^/]+)(/-)?/"
        r"(?:blob|tree)/(?P<rev>[^/]+)/(?P<file>[^#]+)"
        r"(?:#L(?P<line>\d+)|#(?P<anchor>[a-z][a-zA-Z0-9_-]+))?",
        input_url,
    ):
        filename = (
            re.sub(r"\.(adoc|md)$", "", m.group("file")) if m.group("anchor") else m.group("file")
        )
        filename = filename.strip("/")
        line = f"#{m.group('line')}" if m.group("line") else ""
        anchor = f" > {prettify(m.group('anchor'))}" if m.group("anchor") else ""
        return f"{m.group('project')}/{m.group('repo')}:{filename}{line}{anchor}"
    elif m := re.search(
        r"^https://(?P<host>[^/]*gitlab[^/]*)"
        r"(/(?P<project>[^/]+)/(?P<repo>[^/]+))?/-/snippets/"
        r"(?P<uid>[^/?#]+)",
        input_url,
    ):
        if m.group("project"):
            return f"{m.group('project')}/{m.group('repo')}${m.group('uid')}"
        else:
            return f"{m.group('host')}${m.group('uid')}"
    elif m := re.search(
        r"^https://[^/]*jenkins[^/]*/(?:view/[^/]+/)?job/"
        r"(?P<job>[^/]+)/(?:job/(?P<subjob>[^/]+)/)?(?P<build>\d+)?"
        r"(/artifact/(?P<file>[^?#]+))?",
        input_url,
    ):
        subjob = f":{unquote(unquote(m.group('subjob')))}" if m.group("subjob") else ""
        build = f"#{m.group('build')}" if m.group("build") else ""
        file = f":{m.group('file')}" if m.group("file") else ""
        return f"{m.group('job')}{subjob}{build}{file}"
    elif m := re.search(
        r"^https://.*jenkins.*/blue/organizations/jenkins/"
        r"(?P<job>[^/]+)"
        r"(?:/detail/(?P<subjob>[^/]+)/(?P<build>\d+)/)?"
        r"(?:/activity\?branch=(?P<branch>[^&#]+))?",
        input_url,
    ):
        subjob = (
            f":{unquote(m.group('subjob'))}"
            if m.group("subjob") and m.group("job") != m.group("subjob")
            else ""
        )
        # NB: Essentially, branch == subjob, but we need two names for the regex
        branch = f":{unquote(unquote(m.group('branch')))}" if m.group("branch") else ""
        build = f"#{m.group('build')}" if m.group("build") else ""
        return f"{m.group('job')}{subjob}{branch}{build}"
    elif (
        m := re.search(
            r"^https://.*confluence.*/display/(?P<space>[^/]+)" r"(?:/(?P<title>[^?]+))?", input_url
        )
    ) or (
        m := re.search(
            r"^https://.*confluence.*/pages/(?:viewpage|releaseview)\.action\?"
            r"spaceKey=(?P<space>[^&]+)(?:&title=(?P<title>[^&]+))?",
            input_url,
        )
    ):
        space = m.group("space")
        title = f"/{prettify(m.group('title'))}" if m.group("title") else ""
        return f"{space}{title}"
    elif m := re.search(
        r"^https://(?P<page>\w+\.stackexchange|stackoverflow|askubuntu|serverfault|superuser)\.com/"
        r"(q(uestions)?|a(nswers)?)/(?P<qid>[^/]+)/[^/]+(/(?P<aid>[^/#]+))?",
        input_url,
    ):
        page = (
            m.group("page")
            .replace("stackexchange", "SE")
            .replace("stackoverflow", "SO")
            .replace("askubuntu", "AU")
            .replace("serverfault", "SF")
            .replace("superuser", "SU")
        )
        post = m.group("aid") or m.group("qid")
        return f"{page}#{post}"
    elif m := re.search(
        r"^https://hub.docker.com"
        r"/(?:(?:_|layers/library)|(?:layers|r)/(?P<org>[^/]+))"
        r"/(?P<repo>[^/?#$]+)"
        r"(?:/(?P<tag>[^/?#$]+))?",
        input_url,
    ):
        org = f"{m.group('org')}/" if m.group("org") else ""
        repo = m.group("repo")
        tag = f":{m.group('tag')}" if m.group("tag") else ""
        return f"{org}{repo}{tag}"
    elif m := re.search(
        r"^https://(?P<host>[^/?&]*openshift[^/?&]*)"
        r"(?:/k8s/ns/(?P<namespace>[^/?#]+)/[^/?#]+/(?P<resource_name>[^/?#]+))?"
        r"(?:/monitoring/dashboards/(?P<dashboard>[^/?#]+)\?(?P<dashboard_options>[^#$]+))?",
        input_url,
    ):
        if namespace := m.group("namespace"):
            resource_name = m.group("resource_name")
            return f"{namespace}/{resource_name}"
        if options := m.group("dashboard_options"):  # noqa: RET503 -- false positive
            options = dict([option.split("=") for option in options.split("&")])
            if namespace := options.get("namespace"):
                cluster = f"{options['cluster']}/" if options.get("cluster") else ""
                resource_type = f"{options['type'].title()}s " if options.get("type") else ""
                return f"{cluster}{namespace} > {resource_type}Dashboard"
            else:
                cluster = f"{options['cluster']}" if options.get("cluster") else ""
                host = m.group("host") if not options.get("cluster") else ""
                dashboard = prettify(remove_prefix(m.group("dashboard"), "grafana-dashboard-"))
                return f"{host}{cluster} > {dashboard}"
    elif m := re.search(r"\w+://(www\d*\.)?(?P<path>[^?]+)", input_url):
        return m.group("path").strip(" /")
    else:
        # This doesn't even try to look like a URL -- NOP
        return input_url


if __name__ == "__main__":
    print(determine_label(sys.argv[1]))  # pragma: no cover
