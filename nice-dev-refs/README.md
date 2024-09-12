This package takes URLs from the clipboard and pastes them in useful forms.

### Usage

Select a URL, copy it to the clipboard (CTRL+V), and
then type any of the following:

- `:mdref` – paste as Markdown link, i.e. `[label](url)`.
- `:adref` – paste as AsciiDoc link, i.e. `link:url[label]`.
- `:jiraref` – paste as Jira Markup link, i.e. `[label|url]`.
- `:htmlref` – paste as HTML link, i.e. `<a  href="url">label</a>`.
- `:ref` – paste as rich-text link.

### Supported URL Formats

- Email links, i.e. `mailto:`
- **Bitbucket**: project, repository, 
                 pull request (& comment, commit, file & line),
                 file (& line), file (& line) in pull request,
                 commit (& file), branch, tag, diff,
                 search
- **Confluence**: page (& section, comment), space
- **DockerHub**: repository (& tag)
- **GitHub**: repository, branch, commit,
              issue (& comment), discussion (& comment),
              pull request, file (& line), release, heading in rendered file,
              wiki page (& heading), gist (& file & line),
              advisories, enterprises
- **GitLab**: repository, commit,
              issue, merge request, file (& line), snippet,
              heading in rendered file
- **Jenkins**
    - build artifacts
    - classic: "simple" job (& build), multi-branch pipeline (& build);
    - BlueOcean: job build, multi-branch pipeline build
- **Jira**: project, issue (& comment)
- **MS Teams**: channels, messages in channels
- **OpenShift**: project, workload, storage, (some) dashboard(s)
- **Stack Exchange**: question, answer
- **YouTrack**: issue (& comment)

If no format matches, (a trimmed version of) the URL itself is used as link text.
