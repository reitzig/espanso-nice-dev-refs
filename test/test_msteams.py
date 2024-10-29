from assertpy import assert_that

from label_for_url import determine_label


def test_should_label_channel() -> None:
    # Given:
    url = (
        "https://teams.microsoft.com/l/channel/19%3A7e30ad38ade249ecbb3c7d14691173be%40thread.tacv2/"
        "%C3%96ffentlicher%20Kanal%20-%20Allgemein"
        "?groupId=631aa30f-a4a5-4df5-8d04-eaf02eecacbb&tenantId=631aa30f-a4a5-4df5-8d04-eaf02eecacbb"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("Öffentlicher Kanal - Allgemein")


def test_should_label_message_in_channel() -> None:
    # Given:
    url = (
        "https://teams.microsoft.com/l/message/19:60e9051eaa2241239476f00f63f07a80@thread.tacv2/1688399036106"
        "?tenantId=631aa30f-a4a5-4df5-8d04-eaf02eecacbb"
        "&groupId=631aa30f-a4a5-4df5-8d04-eaf02eecacbb"
        "&parentMessageId=1688399036106"
        "&teamName=Our%20(fancy)%20Team"
        "&channelName=Some%20Channel"
        "&createdTime=1688399036106"
        "&allowXTenantAccess=false"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("Our (fancy) Team > Some Channel > #1688399036106")


# editorconfig-checker-disable
# Message in Chat:
# https://teams.microsoft.com/l/message/19:60e9051eaa2241239476f00f63f07a80@thread.v2/1689154388347?context=%7B%22contextType%22%3A%22chat%22%7D
# 🤷

# Team:
# https://teams.microsoft.com/l/team/19%3AGVXGR8HsOW09lCOQldMX-s96lQDcasdWlpFAm3l00HM1%40thread.tacv2/conversations?groupId=631aa30f-a4a5-4df5-8d04-eaf02eecacbb&tenantId=631aa30f-a4a5-4df5-8d04-eaf02eecacbb
# 🤷
# editorconfig-checker-enable
