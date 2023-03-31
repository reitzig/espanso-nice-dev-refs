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


def test_should_label_file_and_line():
    # Given:
    url = "https://github.com/my-account/some-repo/blob/main/some/file.md#L77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('my-account/some-repo:some/file.md#77')


def test_should_label_gist():
    # https://gist.github.com/reitzig/6582edd485a5d0a8b68600dab3b0861b
    # Given:
    url = "https://gist.github.com/my-account/abcdef123456789"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label) \
        .is_equal_to('my-account/abcdef123456789')
