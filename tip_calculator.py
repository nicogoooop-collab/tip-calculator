def calculate_tips(meal_price, custom_tip):
    price = float(meal_price.replace("$", ""))
    custom_pct = float(custom_tip.replace("%", ""))


    tip_15 = price * 0.15
    tip_20 = price * 0.20
    tip_custom = price * (custom_pct / 100)

 
    return [
        f"${tip_15:.2f}",
        f"${tip_20:.2f}",
        f"${tip_custom:.2f}"
        }
