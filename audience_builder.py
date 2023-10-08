# Author: Oluwafemi Olasegiri
# Organization: CareerOnDemand
# this class handle the SuperPixel sheet
# It model the data according to the give data
# It allows to process data after the order of the style of the SuperPixel excel sheet

class AudienceBuilder:
    def __init__(self, ad_spend=['ad_spend', 1000.0, 1000.0, 0], average_order_value=['average_order_value', 197.0, 197.0, None], 
                 total_sales=['total_sales', None, None, None], cpa=['cpa', None, None, None], revenue=['revenue', None, None, None], 
                 total_profit_after_adspend=['total_profit_after_adspend', None, None, None], 
                 site_conversion_rate=['site_conversion_rate', 2.0, 3.0, None], click_through_rate=['click_through_rate', 2.0, 3.5, None], 
                 clicks=['clicks', None, None, None], cost_per_click=['cost_per_click', None, None, None], 
                 impression_needed=['impression_needed', None, None, None], 
                 cost_per_1000_impressions=['cost_per_1000_impressions', 40.0, 35.0, None], 
                 cost_per_1_impressions=['cost_per_1_impressions', None, None, None]
                ):
        
        self.ad_spend = ad_spend
        self.average_order_value = average_order_value if average_order_value[3] is not None else self.get_average_order_value(average_order_value)
        self.total_sales = total_sales if total_sales[3] is not None else self.get_total_sales()
        self.cpa = cpa if cpa[3] is not None else self.get_cpa()
        self.revenue = revenue if revenue[3] is not None else self.get_revenue()
        self.total_profit_after_adspend = total_profit_after_adspend
        self.site_conversion_rate = site_conversion_rate if site_conversion_rate[3] is not None else self.get_site_conversion_rate(site_conversion_rate)
        self.click_through_rate = click_through_rate if click_through_rate[3] is not None else self.get_click_through_rate(click_through_rate)
        self.clicks = clicks if clicks[3] is not None else self.get_clicks()
        self.cost_per_click = cost_per_click if cost_per_click[3] is not None else self.get_cost_per_click()
        self.impression_needed = impression_needed if impression_needed[3] is not None else self.get_impression_needed(impression_needed)
        self.cost_per_1000_impressions = cost_per_1000_impressions if cost_per_1000_impressions[3] is not None else self.get_cost_per_1000_impressions(cost_per_1000_impressions)
        self.cost_per_1_impressions = cost_per_1_impressions if cost_per_1_impressions[2] is not None else self.get_cost_per_1_impressions(cost_per_1000_impressions=cost_per_1000_impressions)

    # working
    def get_average_order_value(self, data):
        return [
            data[0],
            data[1],
            data[2],
            (data[2] - data[1])
        ]
    
    def get_total_sales(self):
        return []
    
    # not working
    def get_cpa(self, ad_spend=[], total_sales=[]):
        return []
        # if ad_spend is None: 
        #     ad_spend = self.ad_spend
        # return [
        #     ad_spend[0],
        #     ad_spend[1],
        #     ad_spend[2],
        #     (ad_spend[2] - ad_spend[1])
        # ]
    
    # not working
    def get_revenue(self):
        return []
    
    # not working
    def get_total_profit_after_adspend(self):
        return []

    # not working
    def get_site_conversion_rate(self, data):
        return [
            data[0],
            data[1] / 100.0,
            data[2] / 100.0,
            (data[2] - data[1]) / 100.0
        ]
    
    # not working
    def get_click_through_rate(self, data):
        return [
            data[0],
            data[1] / 100.0,
            data[2] / 100.0,
            (data[2] - data[1]) / 100.0
        ]
    
    # not working
    def get_clicks(self):
        return []
    
    def get_cost_per_click(self):
        return []
    
    # def get_impression_needed(self, ad_spend=[], cost_per_1000_impressions=[]):
    #     if ad_spend is None: ad_spend = self.ad_spend
    #     if cost_per_1000_impressions is None: cost_per_1000_impressions = self.cost_per_1000_impressions
    #     return [
    #         ad_spend[0],
    #         ad_spend[1],
    #         ad_spend[2],
    #         ad_spend[3]
    #     ]
    
    def get_impression_needed(self, ad_spend=[], cost_per_1000_impressions=[]):
        if ad_spend is None: 
            ad_spend = self.ad_spend
        ad_spend = self.ad_spend
        print(ad_spend)
        if cost_per_1000_impressions is None: 
            cost_per_1000_impressions = self.cost_per_1000_impressions
        #cost_per_1000_impressions = self.cost_per_1000_impressions
        # print(cost_per_1000_impressions)
        print()
        return [
            'impression_needed',
            round(ad_spend[1] * 1000.0, 2),
            # 2.0,
            # round(ad_spend[2] / self.get_cost_per_1000_impressions(cost_per_1000_impressions)[2] * 1000.0, 2),
            round(ad_spend[2] * 1000.0, 2),
            # 2.0,
            # round(self.get_cost_per_1000_impressions(cost_per_1000_impressions)[3] * 1000.0, 2),
            round(ad_spend[3] * 1000.0, 2),
            # 2.0
        ]
    
    def get_cost_per_1000_impressions(self, data):
        return [
            data[0],
            data[1],
            data[2],
            (data[1] - data[2])
        ]
        
    def get_cost_per_1_impressions(self, cost_per_1000_impressions=[]):
        if cost_per_1000_impressions is None: 
            cost_per_1000_impressions = self.cost_per_1000_impressions
        return [
            'cost_per_1_impressions',
            round(cost_per_1000_impressions[1]/1000.0, 2),
            round(cost_per_1000_impressions[2]/1000.0, 2),
            round((cost_per_1000_impressions[1] - cost_per_1000_impressions[2]) / 1000.0, 2),
        ]



# Example usage:
ab = AudienceBuilder()
print(ab.ad_spend)
print(ab.average_order_value)
print(ab.click_through_rate)
print(ab.site_conversion_rate)
print(ab.cost_per_1000_impressions)
print(ab.cost_per_1_impressions)
print(ab.impression_needed)
