import git
import pandas as pd
from footings.model import def_meta, def_parameter, def_sensitivity
from footings.validators import isin

try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

MOD_VERSION = importlib_metadata.version("footings_idi_model")

repo = git.Repo(search_parent_directories=True)
GIT_REVISION = repo.head.object.hexsha


param_n_simulations = def_parameter(
    description="The number of simulations to run.", default=1000, dtype=int,
)

param_seed = def_parameter(
    description="The seed passed to numpy.random.seed.", default=42, dtype=int,
)

param_valuation_dt = def_parameter(
    description="The valuation date which reserves are based.", dtype=pd.Timestamp,
)

param_assumption_set = def_parameter(
    description="""The assumption set to use for running the model. Options are :

        * `stat`
        * `gaap`
        * `best-estimate`
    """,
    dtype=str,
    validator=isin(["STAT", "gaap", "best-estimate"]),
)

param_model_type = def_parameter(
    description="""The policy model to deploy. Options are :

        * `determinstic`
        * `stochastic`
    """,
    dtype=str,
    validator=isin(["deterministic", "stochastic"]),
)

param_net_benefit_method = def_parameter(
    description="""The net benefit method. Options are :

        * `NLP` = Net level premium
        * `PT1` = 1 year preliminary term
        * `PT2` = 2 year preliminary term
    """,
    dtype=str,
    validator=isin(["NLP", "PT1", "PT2"]),
)

param_volume_tbl = def_parameter(
    dtype=pd.DataFrame,
    description="The volume table to use with refence to the distribution of policies by attributes.",
)

param_as_of_dt = def_parameter(
    dtype=pd.Timestamp, description="The as of date which birth date will be based.",
)

meta_model_version = def_meta(
    meta=MOD_VERSION, dtype=str, description="The model version generated by versioneer."
)

meta_last_commit = def_meta(
    meta=GIT_REVISION, dtype=str, description="The last git commit."
)

meta_run_date_time = def_meta(
    meta=pd.to_datetime("now"), dtype=pd.Timestamp, description="The run date and time."
)

modifier_ctr = def_sensitivity(default=1.0, dtype=float, description="Modifier for CTR.")

modifier_interest = def_sensitivity(
    default=1.0, dtype=float, description="Interest rate modifier."
)

modifier_incidence = def_sensitivity(
    default=1.0, description="The incidence rate modifier."
)

modifier_lapse = def_sensitivity(default=1.0, description="The withdraw rate modifier")
modifier_mortality = def_sensitivity(
    default=1.0, description="The withdraw rate modifier"
)
