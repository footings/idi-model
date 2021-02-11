---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python38264bitfootingsidimodelylbo5op8py38venv96bbe8dde9f243b396384b5a65162388

execution:
  timeout: -1
---


# Active - Deterministic - ROP Rider

## Valuation Model

### Documentation

```{eval-rst}
.. autoclass:: footings_idi_model.policy_models.AValRopRPMD
```

### Usage

```{code-cell} ipython3
import pandas as pd
from footings_idi_model.policy_models import AValRopRPMD

model = AValRopRPMD(
    policy_id="policy-1",
    gender="M",
    tobacco_usage="N",
    birth_dt=pd.Timestamp("1970-03-26"),
    policy_start_dt=pd.Timestamp("2015-06-02"),
    policy_end_dt=pd.Timestamp("2035-03-26"),
    elimination_period=90,
    idi_market="INDV",
    idi_contract="AS",
    idi_benefit_period="TO65",
    idi_occupation_class="M",
    cola_percent=0.0,
    premium_pay_to_dt=pd.Timestamp("2020-03-31"),
    gross_premium=10.0,
    gross_premium_freq="MONTH",
    benefit_amount=50.0,
    valuation_dt=pd.Timestamp("2020-03-31"),
    assumption_set="stat",
    withdraw_table="01CSO",
    net_benefit_method="NLP",
    rop_return_freq=10,
    rop_return_percent=0.5,
    rop_claims_paid=0,
    rop_future_claims_start_dt=pd.Timestamp("2005-02-10"),
)
```

To run the model call the `run` method.

```{code-cell} ipython3
output = model.run()
```

The model returns a DataFrame of the projected reserves.

```{code-cell} ipython3
output.info()
```

```{code-cell} ipython3
output
```

An audit of the model is ran by calling the `audit` method shown below.

```{code-cell} ipython3
model.audit("Audit-AValRopRPMD.xlsx")
```

The audit file can be downloaded {download}`here.<./Audit-AValRopRPMD.xlsx>`

## Projection Model

### Documentation

To be completed.

### Usage

To be completed.