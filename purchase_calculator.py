
import streamlit as st

st.title("구매대행 수익 계산기")
st.write("판매 금액과 비용을 입력하면 예상 수익을 계산합니다.")

sale_price = st.number_input("판매 금액 (원)", min_value=0, value=50000, step=1000)
purchase_cost = st.number_input("상품 구매 비용 (원)", min_value=0, value=25000, step=1000)
shipping_cost = st.number_input("배송비 (원)", min_value=0, value=5000, step=1000)
other_cost = st.number_input("기타 비용 (원)", min_value=0, value=3000, step=1000)

profit = sale_price - purchase_cost - shipping_cost - other_cost

if sale_price > 0:
    profit_rate = profit / sale_price * 100
else:
    profit_rate = 0

st.subheader("계산 결과")
st.metric("예상 수익", f"{profit:,.0f}원")
st.metric("수익률", f"{profit_rate:.1f}%")
