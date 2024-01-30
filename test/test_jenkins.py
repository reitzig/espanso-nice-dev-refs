from assertpy import assert_that

from label_for_url import determine_label


def test_should_label_old_school_job() -> None:
    # Given:
    url = "https://our-jenkins.my-org.de/job/SOME_job-name/"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("SOME_job-name")


def test_should_label_old_school_job_without_trailing_slash() -> None:
    # Given:
    url = "https://jenkins-old.my-org.de/job/SOME_job-name"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("SOME_job-name")


def test_should_label_old_school_job_build() -> None:
    # Given:
    url = "https://our-jenkins.my-org.de/job/SOME_job-name/77/console"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("SOME_job-name#77")


def test_should_label_old_school_job_build_through_view() -> None:
    # Given:
    url = "https://our-jenkins.my-org.de/view/Fancy/job/SOME_job-name/77/console"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("SOME_job-name#77")


def test_should_label_old_school_multibranch_pipeline() -> None:
    # Given:
    url = "https://our-jenkins.my-org.de/job/SOME_job-name/job/feature%2FJIRA-42-some-task/42/"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("SOME_job-name:feature/JIRA-42-some-task#42")


def test_should_label_blue_ocean_job_build() -> None:
    # Given:
    url = (
        "https://our-jenkins.my-org.de/blue/organizations/jenkins/"
        "SOME_job-name/detail/SOME_job-name/77/pipeline"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("SOME_job-name#77")


def test_should_label_blue_ocean_multibranch_pipeline() -> None:
    # Given:
    url = (
        "https://our-jenkins.my-org.de/blue/organizations/jenkins/"
        "SOME_job-name/detail/feature%2FJIRA-42-some-task/42/pipeline"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("SOME_job-name:feature/JIRA-42-some-task#42")


def test_should_label_blue_ocean_redirect() -> None:
    # Given:
    url = (
        "https://our-jenkins.my-org.de/job/"
        "SOME_job-name/job/fix%252Fsome-bug/25/display/redirect"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("SOME_job-name:fix/some-bug#25")


def test_should_label_blue_ocean_multibranch_pipeline_branch() -> None:
    # Given:
    url = (
        "https://our-jenkins.my-org.de/blue/organizations/jenkins/"
        "SOME_job-name/activity?branch=fix%252Fsome-bug"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("SOME_job-name:fix/some-bug")


def test_should_label_artifact() -> None:
    # Given:
    url = (
        "https://our-jenkins.my-org.de/job/"
        "SOME_job-name/job/fix%252Fsome-bug/77/artifact/some/file.md"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("SOME_job-name:fix/some-bug#77:some/file.md")
