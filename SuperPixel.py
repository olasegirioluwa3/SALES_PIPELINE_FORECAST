# # Author: Oluwafemi Olasegiri
# # Organization: CareerOnDemand
# # this class handle the SuperPixel sheet
# # It model the data according to the give data
# # It allows to process data after the order of the style of the SuperPixel excel sheet

class SuperPixel:
    def __init__(self, monthly_traffic=17500.0, cpa=150.0, 
                 scr=2.0, deal_value=300.0, sales=None,
                 revenue=None, estimated_spend=None, 
                 anon_traffic=None, idr_match=50.0, 
                 customer_matches=None, verified_mp=None,
                 verification=70.0, recovered_leads=None,
                 re_opt_in=10.0, recovered_sales=None,
                 rsr=3.0, recovered_revenue=None, cpm_per_reactivation=0.25):
        self.monthly_traffic = monthly_traffic
        self.cpa = cpa  # cost per acquisition
        self.scr = scr  # sales conversion rate
        self.deal_value = deal_value  # deal value
        self.sales = sales if sales is not None else self._get_sales()
        self.revenue = revenue if revenue is not None else self._get_revenue()
        self.estimated_spend = estimated_spend if estimated_spend is not None else self._get_estimated_spend()
        self.anon_traffic = anon_traffic if anon_traffic is not None else self._get_anon_traffic()
        self.idr_match = idr_match  # ID Resolution Match
        self.customer_matches = customer_matches if customer_matches is not None else self._get_customer_matches()
        self.verification = verification  # verification
        self.verified_mp = verified_mp if verified_mp is not None else self._get_verified_mp()
        self.re_opt_in = re_opt_in  # Re-opt-in
        self.recovered_leads = recovered_leads if recovered_leads is not None else self._get_recovered_leads()
        self.rsr = rsr  # reactivation sales rate
        self.recovered_sales = recovered_sales if recovered_sales is not None else self._get_recovered_sales()
        self.recovered_revenue = recovered_revenue if recovered_revenue is not None else self._get_recovered_revenue()
        self.cpm_per_reactivation = cpm_per_reactivation  # Cost Per Match/Re-activation

    def _get_sales(self):
        return self.monthly_traffic * self.scr

    def _get_revenue(self):
        return self.sales * self.deal_value

    def _get_estimated_spend(self):
        return self.cpa * self.sales

    def _get_anon_traffic(self):
        return self.monthly_traffic - (self.monthly_traffic * self.scr / 100.0)

    def _get_customer_matches(self):
        return self.anon_traffic * self.idr_match / 100

    def _get_verified_mp(self):
        return self.customer_matches * self.verification / 100

    def _get_recovered_leads(self):
        return self.verified_mp * self.re_opt_in / 100

    def _get_recovered_sales(self):
        return self.recovered_leads * self.rsr / 100

    def _get_recovered_revenue(self):
        return self.recovered_sales * self.deal_value

    def get_cpa_after(self):
        return self.get_total() / self.recovered_sales

    def get_total(self):
        return self.verified_mp * self.cpm_per_reactivation


# Example usage:
sp = SuperPixel()
print(sp.get_cpa_after())
