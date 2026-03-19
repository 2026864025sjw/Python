price=int(input("음식 비용:"))
tip_rate=int(input("팁 비율:"))

tip_amount=price*(tip_rate/100)
total_price=price+tip_amount

print(f"총액: {int(total_price)}달러")