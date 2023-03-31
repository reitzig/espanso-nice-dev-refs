This package takes URLs from the clipboard and pastes them in useful forms.

### Usage

Select a URL, copy it to the clipboard (CTRL+V), and 
then type any of the following: 

- `:mdref` -- paste as Markdown link, i.e. `[label](url)`.
- `:adref` -- paste as AsciiDoc link, i.e. `link:url[label]`.
- `:ref` -- paste as rich-text link.

### Supported URL Formats

- **GitHub**: repository, issue, discussion, pull request, file (& line)
- **GitHub Gist**: gist
- **Bitbucket**: repository, pull request, file (& line), file (& line) in pull request
- **Jenkins** 
  - classic: "simple" job (& build), multi-branch pipeline (& build), 
  - BlueOcean: job build, multi-branch pipeline build
- **Jira**: ticket
- **Confluence**: page

If no format matches, (a trimmed version of) the URL itself is used as link text.
