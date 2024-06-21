import pytest
from assertpy import assert_that

from label_for_url import determine_label


@pytest.mark.skip(reason="nyi")
def test_should_label_project() -> None:
    # Given:
    url = "https://our-bitbucket.my-org.de/projects/MY-PROJECT"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("MY-PROJECT")


# editorconfig-checker-disable
# Message in Chat:
# https://teams.microsoft.com/l/message/19:f0a93bc3576e43dea4ebf3501c7e00e3@thread.v2/1689173888347?context=%7B%22contextType%22%3A%22chat%22%7D

# Channel:
# https://teams.microsoft.com/l/channel/19%3a60e9051eaa2246599476f00f63f07a80%40thread.tacv2/CoP%2520CI-CD?groupId=338c661d-660f-40c1-8679-eaab3d74870e&tenantId=09d108e3-818a-4090-b0f3-e85c6497fe4d

# Message in Channel:
# https://teams.microsoft.com/l/message/19:60e9051eaa2246599476f00f63f07a80@thread.tacv2/1688399036106?tenantId=09d108e3-818a-4090-b0f3-e85c6497fe4d&groupId=338c661d-660f-40c1-8679-eaab3d74870e&parentMessageId=1688399036106&teamName=COL_oscare%20connect&channelName=CoP%20CI-CD&createdTime=1688399036106&allowXTenantAccess=false
# editorconfig-checker-enable
