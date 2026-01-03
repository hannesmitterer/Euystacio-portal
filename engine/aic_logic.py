import json

def calculate_stability_roi(naval_distance, gas_flow, hum_funding):
    """
    AIC Stability ROI Formula
    naval_distance: Distance in nm (Target 125)
    gas_flow: MMcf/day (Target 175)
    hum_funding: USD Millions (Target 606)
    """
    # Risk factor increases as naval distance decreases below 125nm
    risk_factor = 1.0 if naval_distance >= 125 else (125 / max(naval_distance, 1))
    
    # Prosperity factor increases with gas flow and funding
    prosperity_factor = (gas_flow / 175) + (hum_funding / 606)
    
    s_roi = round(prosperity_factor / risk_factor, 2)
    return s_roi

# Current Crisis State: Jan 3, 2026
current_data = {
    "stability_roi": 0.12,
    "insurrection_risk": 72,
    "gas_integrity": 88,
    "blockchain_anchor": "0x8a7f9b2ce33b1fe33b1f9b2ce33b1fe33b1f9b2ce33b1f"
}
