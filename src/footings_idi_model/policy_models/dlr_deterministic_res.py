from footings import model, step, def_parameter
from footings.model_tools import frame_add_exposure
from .dlr_deterministic_base import DValBasePM, STEPS


@model(steps=STEPS)
class DValResRPM(DValBasePM):
    """The disabled life reserve (DLR) valuation model for the cost of living adjustment
    (COLA) policy rider.

    This model is a child of the `DValBasePM` with the only change being how the monthly
    benefit is calculated. The base model uses the benefit amount passed while this model
    calculates the benefit as the benefit amount x residual benefit percent.
    """

    residual_benefit_percent = def_parameter(
        dtype=float,
        description="The residual benefit percent to multiply by the benefit amount.",
    )

    @step(
        name="Calculate Monthly Benefits",
        uses=["frame", "residual_benefit_percent", "benefit_amount"],
        impacts=["frame"],
    )
    def _calculate_monthly_benefits(self):
        """Calculate the monthly benefit amount for each duration."""
        self.frame = frame_add_exposure(
            self.frame,
            begin_date=max(self.valuation_dt, self.start_pay_date),
            end_date=self.termination_dt,
            exposure_name="BENEFIT_FACTOR",
            begin_duration_col="DATE_BD",
            end_duration_col="DATE_ED",
        )
        self.frame["BENEFIT_AMOUNT"] = (
            self.frame["BENEFIT_FACTOR"]
            .mul(self.benefit_amount)
            .mul(self.residual_benefit_percent)
            .round(2)
        )


@model
class DProjResRPM(DValBasePM):
    pass
