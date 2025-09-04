from assertpy import assert_that

from label_for_url import determine_label

# TODO:
#   - https://dev.azure.com/someorg/MyProject/_build?definitionId=148 pipeline
#   - https://dev.azure.com/someorg/MyProject/_build?definitionScope=%5Cmyproject%5Csome-repo scope


def test_should_label_project() -> None:
    # Given:
    url = "https://dev.azure.com/someorg/MyProject"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("someorg/MyProject")


def test_should_label_build() -> None:
    # Given:
    url = "https://dev.azure.com/someorg/MyProject/_build/results?buildId=17337"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("someorg/MyProject#17337")


def test_should_label_build_results() -> None:
    # Given:
    url = "https://dev.azure.com/someorg/MyProject/_build/results?buildId=17337&view=results"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("someorg/MyProject#17337")


def test_should_label_build_job() -> None:
    # Given:
    url = "https://dev.azure.com/someorg/MyProject/_build/results?buildId=17337&view=logs&j=6fafddf9-4498-5beb-fab7-a530ed7d4495"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("someorg/MyProject#17337.6fafddf9")


def test_should_label_build_job_alt() -> None:
    # Given:
    url = "https://dev.azure.com/someorg/MyProject/_build/results?buildId=17337&view=logs&s=6fafddf9-4498-5beb-fab7-a530ed7d4495"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("someorg/MyProject#17337.6fafddf9")


def test_should_label_build_job_step() -> None:
    # Given:
    url = "https://dev.azure.com/someorg/MyProject/_build/results?buildId=17337&view=logs&j=6fafddf9-4498-5beb-fab7-a530ed7d4495&t=243134fc-11ad-5285-1bdf-d75b69453775"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("someorg/MyProject#17337.6fafddf9.243134fc")


def test_should_label_build_job_log_line() -> None:
    # Given:
    url = "https://dev.azure.com/someorg/MyProject/_build/results?buildId=17337&view=logs&j=6fafddf9-4498-5beb-fab7-a530ed7d4495&t=243134fc-11ad-5285-1bdf-d75b69453775&l=77"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("someorg/MyProject#17337.6fafddf9.243134fc:77")
