# Author: Oluwafemi Olasegiri
# Organization: CareerOnDemand
# this class handle the Affiliate Program
# It model the data according to the give data
# It allows to process data after the order of the style of the AffiliateProgram excel sheet

class AffiliateProgram:
    def __init__(self, your_plan=2500.0, avg_plan_ref=2500.0, ref_payout=10.0, payout=None, referral_needed_to_be=10.0, 
                 sales_conversion_rate=40.0, response_rate=60.0, conversations_needed=25.0, touch_point_need=42.0
                ):
    
        self.your_plan=your_plan
        self.avg_plan_ref=avg_plan_ref
        self.ref_payout=ref_payout/100
        self.payout = payout if payout is not None else self.get_payout()
        self.referral_needed_to_be = referral_needed_to_be if referral_needed_to_be is not None else self.get_referral_needed_to_be()
        self.sales_conversion_rate=sales_conversion_rate/100
        self.response_rate=response_rate/100
        self.conversations_needed = conversations_needed if conversations_needed is not None else self.get_conversations_needed()
        self.touch_point_need = touch_point_need if touch_point_need is not None else self.get_touch_point_need()

        
    def get_payout(self):
        return self.avg_plan_ref * self.ref_payout

    def get_referral_needed_to_be(self):
        return self.your_plan / self.payout
    
    def get_conversations_needed(self):
        return self.referral_needed_to_be/self.sales_conversion_rate
    
    def get_touch_point_need(self):
        return self.referral_needed_to_be/self.sales_conversion_rate

# Example usage:
ap = AffiliateProgram()
print(ap.get_touch_point_need())
