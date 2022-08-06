from jqdatasdk import *
import jqdatasdk as jq
from jqdatasdk.technical_analysis import *

if __name__ == '__main__':
    jq.auth('15652376661', '198538Bl')
    scu = get_index_stocks('000001.XSHG') + get_index_stocks('399106.XSHE')

    q1 = query(finance.STK_STATUS_CHANGE.code).filter(finance.STK_STATUS_CHANGE.public_status == '正常上市',
                                                      finance.STK_STATUS_CHANGE.code.in_(scu))
    df1 = finance.run_query(q1)
    print(df1)
    securityList = list(df1['code'])
    q = query(valuation.code).filter(valuation.code.in_(securityList)).order_by(valuation.market_cap.asc()).limit(15)
    df = get_fundamentals(q)
    print(df)
    buyList = list(df['code'])
    print(buyList)

    # 定义股票池列表
    security_list1 = '300082.XSHE'
    security_list2 = ['300082.XSHE', '300083.XSHE', ]
    # 计算并输出 security_list1 的 BOLL 值
    upperband, middleband, lowerband = Bollinger_Bands(security_list1, check_date='2021-09-18', timeperiod=20,
                                                       nbdevup=2, nbdevdn=2)
    print('%.2f' % upperband[security_list1])
    print('%.2f' % middleband[security_list1])
    print('%.2f' % lowerband[security_list1])

    # 计算并输出 security_list1 的 MACD 值
    macd_dif, macd_dea, macd_macd = MACD(security_list1, check_date='2021-09-18', SHORT=12, LONG=26, MID=9)
    print('%.2f' % macd_dif[security_list1])
    print('%.2f' % macd_dea[security_list1])
    print('%.2f' % macd_macd[security_list1])

    # 计算并输出 security_list1 的 KDJ 值
    K1, D1, J1 = KDJ(security_list1, check_date='2021-09-18', N=9, M1=3, M2=3)
    print('%.2f' % K1[security_list1])
    print('%.2f' % D1[security_list1])
    print('%.2f' % J1[security_list1])

    # 计算并输出 security_list1 的 VOL 值
    VOL1, MAVOL11, MAVOL12 = VOL(security_list1, check_date='2021-09-18', M1=5, M2=10)
    print('%.2f' % VOL1[security_list1])
    print('%.2f' % MAVOL11[security_list1])
    print('%.2f' % MAVOL12[security_list1])

    # 取得的最近5条包括 end_dt 的天数据
    df = get_bars(security_list1, 5, unit='1d', fields=('date', 'open', 'high', 'low', 'close', 'volume'),
             include_now=True, end_dt='2021-09-18', fq_ref_date=None)
    print(df)

    df = get_price('300082.XSHE', count=2, end_date='2021-09-22', frequency='daily',
                   fields=['open', 'close', 'high', 'low', 'high_limit', 'low_limit', 'volume'])
    print(df['high_limit'])

    df2 = get_price(security_list2, count=1, end_date='2021-09-22', frequency='daily',
                   fields=['open', 'close', 'high', 'low', 'high_limit', 'low_limit', 'volume'])
    print(df2)
    print(df2['open'].values)
    print(df2['low'].values)
