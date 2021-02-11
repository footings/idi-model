import os

import pandas as pd
import pytest
from footings.audit import AuditConfig, AuditStepConfig
from footings.testing import assert_footings_files_equal

from footings_idi_model.extract_models import DisabledLivesValEMD

# import ray


@pytest.fixture
def shutdown_only():
    yield None
    # The code after the yield will run as teardown code.


#     ray.shutdown()


@pytest.fixture(scope="session")
def tempdir(tmpdir_factory):
    dir_name = os.path.dirname(__file__).split("/")[-1]
    return tmpdir_factory.mktemp(dir_name)


base_extract_file = os.path.join(
    "tests", "extract_models", "disabled_lives", "disabled-lives-sample-base.csv"
)
base_extract = pd.read_csv(
    base_extract_file, parse_dates=["BIRTH_DT", "INCURRED_DT", "TERMINATION_DT"]
)
rider_extract_file = os.path.join(
    "tests", "extract_models", "disabled_lives", "disabled-lives-sample-riders.csv"
)
rider_extract = pd.read_csv(rider_extract_file)

CASES = [
    (
        "test_1",
        {
            "base_extract": base_extract,
            "rider_extract": rider_extract,
            "valuation_dt": pd.Timestamp("2020-03-31"),
            "assumption_set": "stat",
        },
    ),
]


@pytest.mark.parametrize("case", CASES, ids=[x[0] for x in CASES])
def test_disabled_lives_deterministic(case, tempdir, shutdown_only):
    # ray.init(num_cpus=1)
    name, parameters = case
    test_file = tempdir.join(f"test-{name}.json")
    expected_file = os.path.join(
        os.path.dirname(__file__), "audit_files", f"expected-{name}.json",
    )
    config = AuditConfig(
        show_signature=False,
        show_docstring=False,
        show_steps=True,
        step_config=AuditStepConfig(
            show_method_name=False,
            show_docstring=False,
            show_uses=True,
            show_impacts=True,
            show_output=True,
            show_metadata=False,
        ),
    )
    DisabledLivesValEMD(**parameters).audit(test_file, config=config)
    exlcude_list = exlcude_list = [
        "*RUN_DATE_TIME",
        "*MODEL_VERSION",
        "*LAST_COMMIT",
    ]
    assert_footings_files_equal(test_file, expected_file, exclude_keys=exlcude_list)