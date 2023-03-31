#!/usr/bin/env python3

import re
import sys
from urllib.parse import unquote


# TODO: ship as package?
#       -> https://espanso.org/docs/packages/package-specification/
#       but: https://github.com/espanso/espanso/discussions/1558
# TODO: refactor into loop over (regexp, lambda)


def determine_label(input_url: str) -> str:
    if m := re.search(r'^https://[^/]*bitbucket[^/]*/projects/(?P<project>[^/]+)/'
                      r'repos/(?P<repo>[^/]+)/pull-requests/(?P<pr>\d+)/'
                      r'(diff#(?P<file>[^?]+)(\?f=(?P<line>\d+))?)?', input_url):
        filename = f":{m.group('file')}" if m.group('file') else ''
        line = f"#{m.group('line')}" if m.group('line') else ''
        return f"{m.group('project')}/{m.group('repo')}#{m.group('pr')}{filename}{line}"
    elif m := re.search(r'^https://[^/]*bitbucket[^/]*/projects/(?P<project>[^/]+)/'
                        r'repos/(?P<repo>[^/]+)(/browse/(?P<file>[^#]+)(?P<line>#\d+)?)?', input_url):
        if m.group('file'):
            line = m.group('line') or ''
            return f"{m.group('project')}/{m.group('repo')}:{m.group('file')}{line}"
        else:
            return f"{m.group('project')}/{m.group('repo')}"
    elif m := re.search(r'^https://[^/]*jira[^/]*/browse/(?P<issue>\w+-\d+)', input_url):
        return m.group('issue')
    elif m := re.search(r'^https://github.com/(?P<project>[^/]+)/(?P<repo>[^/]+)($|/'
                        r'(issues|pull|discussions)/(?P<number>\d+))', input_url):
        number = f"#{m.group('number')}" if m.group('number') else ''
        return f"{m.group('project')}/{m.group('repo')}{number}"
    elif m := re.search(r'^https://github.com/(?P<project>[^/]+)/(?P<repo>[^/]+)/'
                        r'blob/(?P<rev>[^/]+)/(?P<file>[^#]+)(?:#L(?P<line>\d+))?', input_url):
        line = f"#{m.group('line')}" if m.group('line') else ''
        return f"{m.group('project')}/{m.group('repo')}:{m.group('file')}{line}"
    elif m := re.search(r'^https://gist.github.com/(?P<account>[^/]+)/(?P<uid>[a-f0-9]+)$', input_url):
        return f"{m.group('account')}/{m.group('uid')}"
    elif m := re.search(r'^https://[^/]*jenkins[^/]*/(?:view/[^/]+/)?job/'
                        r'(?P<job>[^/]+)/(?:job/(?P<subjob>[^/]+)/)?(?P<build>\d+)?', input_url):
        subjob = f"/{unquote(m.group('subjob'))}" if m.group('subjob') else ''
        build = f"#{m.group('build')}" if m.group('build') else ''
        return f"{m.group('job')}{subjob}{build}"
    elif m := re.search(r'^https://.*jenkins.*/blue/organizations/jenkins/'
                        r'(?P<job>[^/]+)/detail/(?P<subjob>[^/]+)/(?P<build>\d+)/', input_url):
        subjob = f"/{unquote(m.group('subjob'))}" if m.group('job') != m.group('subjob') else ''
        build = f"#{m.group('build')}" if m.group('build') else ''
        return f"{m.group('job')}{subjob}{build}"
    elif (m := re.search(r'^https://.*confluence.*/display/(?P<space>[^/]+)/(?P<title>[^?]+)', input_url)) \
            or (m := re.search(r'^https://.*confluence.*/pages/viewpage\.action\?'
                               r'spaceKey=(?P<space>[^&]+)&title=(?P<title>[^&]+)', input_url)):
        space = m.group('space')
        title = m.group('title').replace('+', ' ')
        return f"{space}/{title}"
    elif m := re.search(r'\w+://(www\d*\.)?(?P<path>[^?]+)', input_url):
        return m.group('path')
    else:
        # TODO: Prompt for title? Access page for HTML title?
        return input_url


if __name__ == '__main__':
    print(determine_label(sys.argv[1]))
