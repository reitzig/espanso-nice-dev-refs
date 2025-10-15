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

- Email links, i.e. `mailto:`; link to text fragment
- **Azure DevOps**: project,
                    build (& job & step & log line)
- **Bitbucket**: project, repository, 
                 pull request (& comment, commit, file & line),
                 file (& line), file (& line) in pull request,
                 commit (& file), branch, tag, diff,
                 search
- **Confluence**: page (& section, comment), space,
                  blog post (& comment)
- **DockerHub**: repository (& tag)
- **GitHub**: repository, branch, commit (& diff & line),
              issue (& comment, search),
              discussion (& comment),
              pull request (& comment, search, diff lines) 
              file (& line), 
              release, heading in rendered file,
              wiki page (& heading), gist (& file & line),
              advisories, enterprises, organizations
- **GitLab**: (sub)group, repository, commit (& diff),
              issue (& comment, search),
              merge request (& comment, search),
              pipeline, job,
              file (& line), snippet,
              heading in rendered file
- **Gitea**: repository, branch (& diff), commit (& diff),
              pull request (& comment) 
              file (& line), 
- **Jenkins**
    - build artifacts
    - classic: "simple" job (& build), multi-branch pipeline (& build), view;
    - BlueOcean: job build, multi-branch pipeline build
- **Jira**: project, issue (& comment), service desk tickets
- **MS Teams**: channels, messages in channels
- **OpenShift**: project, workload, storage, (some) dashboard(s)
- **Stack Exchange**: question, answer
- **YouTrack**: issue (& comment)

If no format matches, (a trimmed version of) the URL itself is used as link text.
