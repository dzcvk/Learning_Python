CNTx = [0]*4
TCLKx = [1/2, 1/8, 1/32, 1/128]

MCK = 84000000

N_ms = input("Please type in the time you need (ms)\n"+
             ">>> ")
N_ms = int(N_ms)
#CMPx = input("Please type in the compare register\n"+
#            "0: RC"+
#             "1: RB"+
#             "2: RA")
#Rx = ["RC", "RB", "RA"]

for index in range(4):
    CNTx[index] = TCLKx[index]*N_ms*(MCK/1000)

for index in range(4):
    if(CNTx[index] > 65535):
        print(str(index)+": if you use TCLK"+str(index+1)+" overflow!")
    else:
        print(str(index)+": if you use TLCK"+str(index+1)+" is "+str(CNTx[index]))
N_TCLK = input("Which Clock signal do you want to use?\n"+
               ">>> ")



N_CLK = input("Which Timer do you want to use?\n"+
              "0: TC0\n"+
              "1: TC1\n"+
              "2: TC2\n"+
              ">>> ")

N_CHN = input("Which channel do you want to use?\n"+
              "0: CHN1\n"+
              "1: CHN2\n"+
              "2: CHN3\n"+
              ">>> ")

########### REG_TCx_WPMR ###########
print("REG_TC"+N_CLK+"WPMR = 0x54494d00;")

########### REG_TCx_CMRx ###########
print("REG_TC"+N_CLK+"CMR"+N_CHN+" = "+
      "0b"+
                #TIOB
      "00"+     #BSWTRG     bit30
      "00"+     #BEEVT      bit28
      "00"+     #BCPC       bit26
      "00"+     #BCPB       bit24
      
                #TIOA
      "00"+     #ASWTRG     bit22
      "00"+     #AEEVT      bit20
      "00"+     #ACPC       bit18       
      "00"+     #ACPA       bit16
      
      "1"+      #WAVE       bit15       Configured as Waveform mode
      "10"+     #WAVSEL     bit13       RC configured as UP with trigger mode
      "0"+      #ENETRG     bit12
      "00"+     #EEVT       bit10
      "00"+     #EEVTEDG    bit8
      "0"+      #CPCDIS     bit7
      "0"+      #CPCSTOP    bit6
      "00"+     #BURST      bit4
      "0"+      #CLKI       bit3
      str(bin(int(N_TCLK))[2:])+
                #TCCLKS     bit0
      ";")

########### REG_TCx_RXx ###########
print("REG_TC"+N_CLK+"RC"+N_CHN+" = "+str(hex(int(CNTx[int(N_TCLK)])))+";")

########### REG_TCx_IERx ###########
print("REG_TC"+N_CLK+"IER"+N_CHN+" = "+
      "0b"+
      "0"+      #ETRGS
      "0"+      #LDRBS
      "0"+      #LDRAS
      "1"+      #CPCS                   RC compare interrupt activated
      "0"+      #CPBS
      "0"+      #CPAS
      "0"+      #LOVRS
      "0"+      #COVFS
      ";")

########### NVIC ###########
print("NVIC_EnableIRQ(TC"+N_CLK+"_IRQn);")

########### REG_TCx_CCRx ###########
print("REG_TC"+N_CLK+"CCR"+N_CHN+" = "+
      "0b"+
      "1"+      #SWTRG                  Reset the CV
      "0"+      #CLKDIS
      "1"+      #CLKEN                  Enable the clock, start counting
      ";")
