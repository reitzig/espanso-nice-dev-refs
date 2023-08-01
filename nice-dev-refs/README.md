This package takes URLs from the clipboard and pastes them in useful forms.

### Usage

Select a URL, copy it to the clipboard (CTRL+V), and 
then type any of the following: 

- `:mdref` -- paste as Markdown link, i.e. `[label](url)`.
- `:adref` -- paste as AsciiDoc link, i.e. `link:url[label]`.
- `:jiraref` -- paste as Jira Markup link, i.e. `[label|url]`.
- `:ref` -- paste as rich-text link.

### Supported URL Formats

- **GitHub**: repository, issue (& comment), discussion (& comment), 
              pull request, file (& line), release, heading in rendered file, 
              wiki page (& heading), gist (& file & line)
- **GitLab**: repository, issue, merge request, file (& line), snippet,
              heading in rendered file
- **Stack Exchange**: question, answer
  - **Bitbucket**: project, repository, 
                   pull request (& comment, commit, file & line), 
                   file (& line), file (& line) in pull request,
                   commit (& file), branch, diff
- **Jenkins**
    - build artifacts
    - classic: "simple" job (& build), multi-branch pipeline (& build);
    - BlueOcean: job build, multi-branch pipeline build
- **Jira**: project, issue (& comment)
- **Confluence**: page

If no format matches, (a trimmed version of) the URL itself is used as link text.
