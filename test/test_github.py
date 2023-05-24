from assertpy import assert_that

from label_for_url import determine_label


def test_should_label_repository():
    # Given:
    url = "https://github.com/my-account/some-repo"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('my-account/some-repo')


def test_should_label_repo_and_anchor():
    # Given:
    url = "https://github.com/my-account/some-repo#some-headline"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('my-account/some-repo > Some Headline')


def test_should_label_issue():
    # Given:
    url = "https://github.com/my-account/some-repo/issues/77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('my-account/some-repo#77')


def test_should_label_issue_and_comment():
    # Given:
    url = "https://github.com/my-account/some-repo/issues/77#issuecomment-42"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('my-account/some-repo#77.42')


def test_should_label_discussion():
    # Given:
    url = "https://github.com/my-account/some-repo/discussions/42"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('my-account/some-repo#42')


def test_should_label_pr():
    # Given:
    url = "https://github.com/my-account/some-repo/pull/119"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('my-account/some-repo#119')


def test_should_label_file():
    # Given:
    url = "https://github.com/my-account/some-repo/blob/main/some/file.md"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('my-account/some-repo:some/file.md')


def test_should_label_folder():
    # Given:
    url = "https://github.com/my-account/some-repo/tree/main/some/folder"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('my-account/some-repo:some/folder')


def test_should_label_folder_and_anchor():
    # Given:
    url = "https://github.com/my-account/some-repo/tree/main/some/folder#some-headline"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('my-account/some-repo:some/folder > Some Headline')


def test_should_label_file_and_line():
    # Given:
    url = "https://github.com/my-account/some-repo/blob/main/some/file.md#L77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('my-account/some-repo:some/file.md#77')


def test_should_label_markdown_and_anchor():
    # Given:
    url = "https://github.com/my-account/some-repo/blob/main/some/README.md#some-headline"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('my-account/some-repo:some/README > Some Headline')


def test_should_label_release():
    url = "https://github.com/my-account/some-repo/releases/tag/1.2.3"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('my-account/some-repo@1.2.3')


def test_should_label_gist():
    # Given:
    url = "https://gist.github.com/my-account/abcdef123456789"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('my-account/abcdef')


def test_should_label_gist_and_file():
    # Given:
    url = "https://gist.github.com/my-account/abcdef123456789#file-some_file-md"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('my-account/abcdef:some_file-md')
    # NB: We won't be able to determine which parts are file endings


def test_should_label_gist_and_file_and_line():
    # Given:
    url = "https://gist.github.com/my-account/abcdef123456789#file-some_file-md-L42"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('my-account/abcdef:some_file-md#42')
    # NB: We won't be able to determine which parts are file endings


def test_should_label_wiki_page():
    # Given:
    url = "https://github.com/my-account/some-repo/wiki/Some-Page"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('my-account/some-repo > Some Page')


def test_should_label_wiki_page_and_anchor():
    # Given:
    url = "https://github.com/my-account/some-repo/wiki/Some-Page#some-headline"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('my-account/some-repo > Some Page > Some Headline')
