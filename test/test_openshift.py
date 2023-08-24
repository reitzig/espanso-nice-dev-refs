from assertpy import assert_that

from label_for_url import determine_label


def test_should_label_pod() -> None:
    # Given:
    url = "https://console-openshift.some.org/k8s/ns/some-ns/pods/pod-name-fvct8"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("some-ns/pod-name-fvct8")


def test_should_label_cronjob() -> None:
    # Given:
    url = "https://console-openshift.some.org/k8s/ns/some-ns/cronjobs/my-job"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("some-ns/my-job")


def test_should_label_configmap() -> None:
    # Given:
    url = "https://console-openshift.some.org/k8s/ns/some-ns/configmaps/my-config"

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("some-ns/my-config")


def test_should_label_metrics_dashboard_workload_jobs() -> None:
    # Given:
    url = (
        "https://console-openshift.some.org/monitoring/dashboards/"
        "grafana-dashboard-k8s-resources-workloads-namespace"
        "?cluster=my-cluster&namespace=some-ns&type=job&timeRange=172800000"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-cluster/some-ns > Jobs Dashboard")


def test_should_label_metrics_dashboard_pods() -> None:
    # Given:
    url = (
        "https://console-openshift.some.org/monitoring/dashboards/"
        "grafana-dashboard-k8s-resources-namespace"
        "?cluster=my-cluster&namespace=some-ns"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-cluster/some-ns > Dashboard")


def test_should_label_metrics_dashboard_networking() -> None:
    # Given:
    url = (
        "https://console-openshift.some.org/monitoring/dashboards/"
        "grafana-dashboard-namespace-by-pod"
        "?namespace=some-ns&resolution=5m&interval=4h&cluster=my-cluster"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("my-cluster/some-ns > Dashboard")


def test_should_label_metrics_dashboard_api() -> None:
    # Given:
    url = (
        "https://console-openshift.some.org/monitoring/dashboards/"
        "grafana-dashboard-api-performance"
        "?period=5m&apiserver=kube-apiserver"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("console-openshift.some.org > Api Performance")


def test_should_label_metrics_dashboard_etcd() -> None:
    # Given:
    url = (
        "https://console-openshift.some.org/monitoring/dashboards/" "etcd-dashboard" "?cluster=etcd"
    )

    # When:
    label = determine_label(url)

    # Then:
    assert_that(label).is_equal_to("etcd > Etcd Dashboard")
