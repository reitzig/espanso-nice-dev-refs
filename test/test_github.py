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


def test_should_label_issue():
    # Given:
    url = "https://github.com/my-account/some-repo/issues/77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('my-account/some-repo#77')


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


def test_should_label_file_and_line():
    # Given:
    url = "https://github.com/my-account/some-repo/blob/main/some/file.md#L77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('my-account/some-repo:some/file.md#77')


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
