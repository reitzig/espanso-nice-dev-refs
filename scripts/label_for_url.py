#!/usr/bin/env python3

import re
import sys
from urllib.parse import unquote


def determine_label(input_url: str) -> str:
    if m := re.search(r'^https://[^/]*bitbucket[^/]*/projects/(?P<project>[^/]+)/repos/(?P<repo>[^/]+)/'
                      r'(pull-requests/(?P<pr>\d+)|commits/(?P<commit>[a-fA-F0-9]+))/?'
                      r'((diff)?#(?P<file>[^?]+)(\?f=(?P<line>\d+))?)?'
                      r'(overview\?commentId=(?P<comment>\d+))?', input_url):
        pr = f"#{m.group('pr')}" if m.group('pr') else ''
        commit = f"@{m.group('commit')[0:8]}" if m.group('commit') else ''
        filename = f":{m.group('file')}" if m.group('file') else ''
        line = f"#{m.group('line')}" if m.group('line') else ''
        comment = f".{m.group('comment')}" if m.group('comment') else ''
        return f"{m.group('project')}/{m.group('repo')}{pr}{commit}{filename}{line}{comment}"
    elif m := re.search(r'^https://[^/]*bitbucket[^/]*/projects/(?P<project>[^/]+)/repos/(?P<repo>[^/]+)/'
                        r'compare/(commits|diff)\?sourceBranch=refs%2Fheads%2F(?P<branch>[^&]+)', input_url):
        branch = unquote(m.group('branch'))
        return f"{m.group('project')}/{m.group('repo')}@{branch}"
    elif m := re.search(r'^https://[^/]*bitbucket[^/]*/projects/(?P<project>[^/]+)'
                        r'(/repos/(?P<repo>[^/]+))?'
                        r'(/browse/(?P<file>[^#]+)(?P<line>#\d+)?)?', input_url):
        repo = f"/{m.group('repo')}" if m.group('repo') else ''
        filename = f":{m.group('file')}" if m.group('file') else ''
        line = m.group('line') or ''
        return f"{m.group('project')}{repo}{filename}{line}"
    elif m := re.search(r'^https://[^/]*jira[^/]*/browse/(?P<issue>\w+-\d+)', input_url):
        return m.group('issue')
    elif m := re.search(r'^https://gist.github.com/(?P<account>[^/]+)/'
                        r'(?P<uid>[a-f0-9]+)(?:#file-(?P<fileline>[^?]+))?$', input_url):
        # Take apart the wicked file-line format:
        fileline_parts = m.group('fileline').split('-') if m.group('fileline') else None
        filename_parts, line_part = [fileline_parts[0:-1], fileline_parts[-1]] \
            if fileline_parts and re.search(r'^L\d+$', fileline_parts[-1]) \
            else [fileline_parts, '']

        filename = f":{'-'.join(filename_parts)}" if fileline_parts else ''
        line = f"#{line_part.replace('L', '')}" if line_part else ''
        return f"{m.group('account')}/{m.group('uid')[0:6]}{filename}{line}"
    elif m := re.search(r'^https://[^/]*git(hub|lab)[^/]*/(?P<project>[^/]+)/(?P<repo>[^/]+)(/-)?($|/'
                        r'(issues|pull|discussions|merge_requests)/(?P<number>\d+))', input_url):
        number = f"#{m.group('number')}" if m.group('number') else ''
        return f"{m.group('project')}/{m.group('repo')}{number}"
    elif m := re.search(r'^https://[^/]*git(hub|lab)[^/]*/(?P<project>[^/]+)/(?P<repo>[^/]+)(/-)?/'
                        r'(?:blob|tree)/(?P<rev>[^/]+)/(?P<file>[^#]+)(?:#L(?P<line>\d+))?', input_url):
        line = f"#{m.group('line')}" if m.group('line') else ''
        return f"{m.group('project')}/{m.group('repo')}:{m.group('file')}{line}"
    elif m := re.search(r'^https://(?P<host>[^/]*gitlab[^/]*)'
                        r'(/(?P<project>[^/]+)/(?P<repo>[^/]+))?/-/snippets/'
                        r'(?P<uid>[^/?#]+)', input_url):
        if m.group('project'):
            return f"{m.group('project')}/{m.group('repo')}${m.group('uid')}"
        else:
            return f"{m.group('host')}${m.group('uid')}"
    elif m := re.search(r'^https://[^/]*jenkins[^/]*/(?:view/[^/]+/)?job/'
                        r'(?P<job>[^/]+)/(?:job/(?P<subjob>[^/]+)/)?(?P<build>\d+)?', input_url):
        subjob = f":{unquote(unquote(m.group('subjob')))}" if m.group('subjob') else ''
        build = f"#{m.group('build')}" if m.group('build') else ''
        return f"{m.group('job')}{subjob}{build}"
    elif m := re.search(r'^https://.*jenkins.*/blue/organizations/jenkins/'
                        r'(?P<job>[^/]+)/detail/(?P<subjob>[^/]+)/(?P<build>\d+)/', input_url):
        subjob = f":{unquote(m.group('subjob'))}" if m.group('job') != m.group('subjob') else ''
        build = f"#{m.group('build')}" if m.group('build') else ''
        return f"{m.group('job')}{subjob}{build}"
    elif (m := re.search(r'^https://.*confluence.*/display/(?P<space>[^/]+)/(?P<title>[^?]+)', input_url)) \
            or (m := re.search(r'^https://.*confluence.*/pages/viewpage\.action\?'
                               r'spaceKey=(?P<space>[^&]+)&title=(?P<title>[^&]+)', input_url)):
        space = m.group('space')
        title = unquote(m.group('title').replace('+', ' ')).strip()
        return f"{space}/{title}"
    elif m := re.search(r'^https://(?P<page>\w+\.stackexchange|stackoverflow|askubuntu|serverfault|superuser)\.com/'
                        r'(q(uestions)?|a(nswers)?)/(?P<qid>[^/]+)/[^/]+(/(?P<aid>[^/#]+))?', input_url):
        page = m.group('page')\
            .replace('stackexchange', 'SE')\
            .replace('stackoverflow', 'SO')\
            .replace('askubuntu', 'AU')\
            .replace('serverfault', 'SF')\
            .replace('superuser', 'SU')
        post = m.group('aid') or m.group('qid')
        return f"{page}#{post}"
    elif m := re.search(r'\w+://(www\d*\.)?(?P<path>[^?]+)', input_url):
        return m.group('path').strip(" /")
    else:
        # This doesn't even try to look like a URL -- NOP
        return input_url


if __name__ == '__main__':
    print(determine_label(sys.argv[1]))
