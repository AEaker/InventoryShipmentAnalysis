import pandas as pd
import numpy as np
import datetime



def CullInvReport(CompletedServicesDF, ideal):
     CompletedServicesDF = CompletedServicesDF.iloc[:, [1,2,3,7,8]]
     CompletedServicesDF = CompletedServicesDF[CompletedServicesDF["90 Day Usage"] != 0]
     CompletedServicesDF["Daily Consumption"] = CompletedServicesDF["30 Day Usage"]/30
     mergedf = pd.merge(CompletedServicesDF, ideal, on=["Part Number", "Description"])
     return mergedf

# def WHCompliance(mergedf):
#      mergedf = mergedf[(mergedf["Comments"] != "Irrelevant") & (mergedf["Comments"] != "Obsolete")]
#      mergedf.loc[mergedf["On Hand"] > mergedf["Ideal Max"], "WarehouseCompliance"] = "Overstock"
#      mergedf.loc[mergedf["Comments"] == "TBD", "WarehouseCompliance"] = "TBD..."
#      mergedf["WarehouseCompliance"].fillna("Complaint", inplace=True)

#      return mergedf

def AllocationsForecastAndSupply(Allocations, Forecast,  mergedf):
     todaysdate = datetime.date.today()
     year, week_num, day_of_week = todaysdate.isocalendar()
     todaysnumber = datetime.datetime.today().weekday() + 1


     mergedf = mergedf[(mergedf["Comments"] != "Irrelevant") & (mergedf["Comments"] != "Obsolete")]
     mergedf.loc[mergedf["On Hand"] > mergedf["Ideal Max"], "Warehouse Compliance"] = "Overstock"
     mergedf.loc[mergedf["Comments"] == "TBD", "Warehouse Compliance"] = "TBD..."
     mergedf["Warehouse Compliance"].fillna("Complaint", inplace=True)

     UpdatedForecast = Forecast[(Forecast["KNR Week"] > week_num) & (Forecast["KNR Day"] >= todaysnumber)]

     ABACount = Allocations.loc[Allocations["SVCCD"] == "ABA", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("ABA").sum()
     AGGCount = Allocations.loc[Allocations["SVCCD"] == "AGG", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("AGG").sum() + Allocations.loc[Allocations["SVCCD"] == "ZA3", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("ZA3").sum() + Allocations.loc[Allocations["SVCCD"] == "CGG", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("CGG").sum()
     ABCCount = Allocations.loc[Allocations["SVCCD"] == "ABC", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("ABC").sum() + Allocations.loc[Allocations["SVCCD"] == "ZA3", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("ZA3").sum()
     ACCCount =  Allocations.loc[Allocations["SVCCD"] == "ACC", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("ACC").sum()
     ACKCount =  Allocations.loc[Allocations["SVCCD"] == "ACK", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("ACK").sum()
     AGHCount =  Allocations.loc[Allocations["SVCCD"] == "AGH", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("AGH").sum()
     ALNCount =  Allocations.loc[Allocations["SVCCD"] == "ALN", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("ALN").sum()
     AMCCount =  Allocations.loc[Allocations["SVCCD"] == "AMC", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("AMC").sum() + Allocations.loc[Allocations["SVCCD"] == "ZA1", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("ZA1").sum()
     AMKCount =  Allocations.loc[Allocations["SVCCD"] == "AMK", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("AMK").sum() + Allocations.loc[Allocations["SVCCD"] == "ZA2", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("ZA2").sum()
     AtlasTrunkLinerCount = AMKCount + AMCCount
     APCCount =  Allocations.loc[Allocations["SVCCD"] == "APC", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("APC").sum() + Allocations.loc[Allocations["SVCCD"] == "ZA1", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("ZA1").sum() + Allocations.loc[Allocations["SVCCD"] == "ZA2", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("ZA2").sum()
     B_Mirror_Count =  Allocations.loc[Allocations["SVCCD"] == "ARV", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("ARV").sum() + Allocations.loc[Allocations["SVCCD"] == "ZA1", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("ZA1").sum() + Allocations.loc[Allocations["SVCCD"] == "ZA2", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("ZA2").sum() + Allocations.loc[Allocations["SVCCD"] == "BRM", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("BRM").sum() + Allocations.loc[Allocations["SVCCD"] == "ZC1", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("ZC1").sum()
     ATHCount = Allocations.loc[Allocations["SVCCD"] == "ATH", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("ATH").sum()
     ATSCount = Allocations.loc[Allocations["SVCCD"] == "ATS", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("ATS").sum() + Allocations.loc[Allocations["SVCCD"] == "ZA3", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("ZA3").sum()
     AWDCount = Allocations.loc[Allocations["SVCCD"] == "AWD", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("AWD").sum() + Allocations.loc[Allocations["SVCCD"] == "CWD", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("CWD").sum()
     BDPCount = Allocations.loc[Allocations["SVCCD"] == "BDP", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("BDP").sum() + Allocations.loc[Allocations["SVCCD"] == "BLR", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("BLR").sum()
     BKMCount = Allocations.loc[Allocations["SVCCD"] == "BKM", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("BKM").sum()
     BLNCount = Allocations.loc[Allocations["SVCCD"] == "BLN", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("BLN").sum()
     BMJCount = Allocations.loc[Allocations["SVCCD"] == "BMJ", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("BMJ").sum()
     BRECount = Allocations.loc[Allocations["SVCCD"] == "BRE", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("BRE").sum()
     RoadsideCount = Allocations.loc[Allocations["SVCCD"] == "BRK", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("BRK").sum() + Allocations.loc[Allocations["SVCCD"] == "BSK", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("BSK").sum()
     FirstAidCount = Allocations.loc[Allocations["SVCCD"] == "FAK", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("FAK").sum() + Allocations.loc[Allocations["SVCCD"] == "BSK", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("BSK").sum()
     BSGCount =  Allocations.loc[Allocations["SVCCD"] == "BSG", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("BSG").sum()
     CBCCount = Allocations.loc[Allocations["SVCCD"] == "CBC", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("CBC").sum()
     CCPCount = Allocations.loc[Allocations["SVCCD"] == "CCP", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("CCP").sum() + Allocations.loc[Allocations["SVCCD"] == "ZC1", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("Zc1").sum()
     CMCCount = Allocations.loc[Allocations["SVCCD"] == "CMC", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("CMC").sum()
     CMKCount = Allocations.loc[Allocations["SVCCD"] == "CMK", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("CMK").sum() + Allocations.loc[Allocations["SVCCD"] == "ZC1", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("ZC1").sum()
     PPMCount = Allocations.loc[Allocations["SVCCD"] == "PPM", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("PPM").sum()
     VPLCount = Allocations.loc[Allocations["SVCCD"] == "VPL", "VWGA"].iloc[0] + UpdatedForecast["Options"].str.count("VPL").sum()

     mergedf.loc[(mergedf["Part Number"] == "3CN061195A DML") & (mergedf["On Hand"] < ABACount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "3CN061195A DML") & (mergedf["On Hand"] > ABACount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "3CN071151A") & (mergedf["On Hand"] < ABCCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "3CN071151A") & (mergedf["On Hand"] > ABCCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "3CN061370D WGK") & (mergedf["On Hand"] < ACCCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "3CN061370D WGK") & (mergedf["On Hand"] > ACCCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "3CN061370E WGK") & (mergedf["On Hand"] < ACKCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "3CN061370E WGK") & (mergedf["On Hand"] > ACKCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "3CM075111") & (mergedf["On Hand"] < AGGCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "3CM075111") & (mergedf["On Hand"] > AGGCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "3CM075101") & (mergedf["On Hand"] < AGGCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "3CM075101") & (mergedf["On Hand"] > AGGCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "3CN092730A") & (mergedf["On Hand"] < AGHCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "3CN092730A") & (mergedf["On Hand"] > AGHCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "7L0055305N") & (mergedf["On Hand"] < AGHCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "7L0055305N") & (mergedf["On Hand"] > AGHCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "3CN065110") & (mergedf["On Hand"] < ALNCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "3CN065110") & (mergedf["On Hand"] > ALNCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "3CN061550C 041") & (mergedf["On Hand"] < AMCCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "3CN061550C 041") & (mergedf["On Hand"] > AMCCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "3CN061550B 041") & (mergedf["On Hand"] < AMKCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "3CN061550B 041") & (mergedf["On Hand"] > AMKCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "3CN061166  469") & (mergedf["On Hand"] < AtlasTrunkLinerCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "3CN061166  469") & (mergedf["On Hand"] > AtlasTrunkLinerCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "3CN061167  ZRX") & (mergedf["On Hand"] < APCCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "3CN061167  ZRX") & (mergedf["On Hand"] > APCCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "000072548B") & (mergedf["On Hand"] < B_Mirror_Count), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "000072548B") & (mergedf["On Hand"] > B_Mirror_Count), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "3CN071691  DML") & (mergedf["On Hand"] < ATSCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "3CN071691  DML") & (mergedf["On Hand"] > ATSCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "3CM072195") & (mergedf["On Hand"] < AWDCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "3CM072195") & (mergedf["On Hand"] > AWDCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "561061195  KS6") & (mergedf["On Hand"] < BDPCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "561061195  KS6") & (mergedf["On Hand"] > BDPCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "561061550E 041") & (mergedf["On Hand"] < BKMCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "561061550E 041") & (mergedf["On Hand"] > BKMCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "561061166  469") & (mergedf["On Hand"] < BKMCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "561061166  469") & (mergedf["On Hand"] > BKMCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "3C5065110") & (mergedf["On Hand"] < BLNCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "3C5065110") & (mergedf["On Hand"] > BLNCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "5610161370E EOM") & (mergedf["On Hand"] < BMJCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "5610161370E EOM") & (mergedf["On Hand"] > BMJCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "561065760B") & (mergedf["On Hand"] < BRECount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "561065760B") & (mergedf["On Hand"] > BRECount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "000093059AH") & (mergedf["On Hand"] < RoadsideCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "000093059AH") & (mergedf["On Hand"] > RoadsideCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "561075111A") & (mergedf["On Hand"] < BSGCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "561075111A") & (mergedf["On Hand"] > BSGCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "561075101B") & (mergedf["On Hand"] < BSGCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "561075101B") & (mergedf["On Hand"] > BSGCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "000093108L 9B9") & (mergedf["On Hand"] < FirstAidCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "000093108L 9B9") & (mergedf["On Hand"] > FirstAidCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "3CM071151") & (mergedf["On Hand"] < CBCCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "3CM071151") & (mergedf["On Hand"] > CBCCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "3CM061167") & (mergedf["On Hand"] < CCPCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "3CM061167") & (mergedf["On Hand"] > CCPCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "3CM061370A WGK") & (mergedf["On Hand"] < CMCCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "3CM061370A WGK") & (mergedf["On Hand"] > CMCCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "3CM061530 82V") & (mergedf["On Hand"] < CMKCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "3CM061530 82V") & (mergedf["On Hand"] > CMKCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "3CM061166 469") & (mergedf["On Hand"] < CMKCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "3CM061166 469") & (mergedf["On Hand"] > CMKCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "000072548H") & (mergedf["On Hand"] < PPMCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "000072548H") & (mergedf["On Hand"] > PPMCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf.loc[(mergedf["Part Number"] == "000052120D") & (mergedf["On Hand"] < VPLCount), "Allocation/Forecast Standing"] = "Less Parts Than Forecasted"
     mergedf.loc[(mergedf["Part Number"] == "000052120D") & (mergedf["On Hand"] > VPLCount), "Allocation/Forecast Standing"] = "More Parts Than Forecasted"

     mergedf["Allocation/Forecast Standing"].fillna("TBD..",inplace=True)

     mergedf["Estimated Supply Life (Weeks)"] = (mergedf["On Hand"]/mergedf["Daily Consumption"])/7
     mergedf["Estimated Supply Life (Weeks)"].replace(np.inf, 0, inplace=True)
     mergedf["Estimated Supply Life (Weeks)"].fillna(0, inplace=True)
     mergedf["Estimated Supply Life (Weeks)"] = mergedf["Estimated Supply Life (Weeks)"].astype(int)
     # .astype(str) + " Weeks"

     return mergedf


