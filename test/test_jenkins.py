from assertpy import assert_that

from label_for_url import determine_label


def test_should_label_old_school_job():
    # Given:
    url = "https://our-jenkins.my-org.de/job/SOME_job-name/"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label)\
        .is_equal_to('SOME_job-name')


def test_should_label_old_school_job_build():
    # Given:
    url = "https://our-jenkins.my-org.de/job/SOME_job-name/77/console"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label)\
        .is_equal_to('SOME_job-name#77')


def test_should_label_old_school_multibranch_pipeline():
    # Given:
    url = "https://our-jenkins.my-org.de/job/SOME_job-name/job/feature%2FJIRA-42-some-task/42/"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label)\
        .is_equal_to('SOME_job-name/feature/JIRA-42-some-task#42')


def test_should_label_blue_ocean_job_build():
    # Given:
    url = "https://our-jenkins.my-org.de/blue/organizations/jenkins/"\
          "SOME_job-name/detail/SOME_job-name/77/pipeline"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label)\
        .is_equal_to('SOME_job-name#77')


def test_should_label_blue_ocean_multibranch_pipeline():
    # Given:
    url = "https://our-jenkins.my-org.de/blue/organizations/jenkins/"\
          "SOME_job-name/detail/feature%2FJIRA-42-some-task/42/pipeline"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label)\
        .is_equal_to('SOME_job-name/feature/JIRA-42-some-task#42')
