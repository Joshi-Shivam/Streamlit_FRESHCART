import streamlit as st
import random as rd
import datetime as dt
import fpdf as pdf
from fpdf import FPDF
from streamlit import session_state
if "fitem" not in st.session_state:
    st.session_state.fitem={
        "Apple": 20,
        "Banana": 10,
        "Orange": 15,
        "Mango": 50,
        "Peach": 40
    }
if "vitem" not in st.session_state:
    st.session_state.vitem={
            "Tomato":10,
            "Onion":12,
            "Cabbage":10,
            "Potato":15,
            "Garlic":5,
            "Spinach":20
      }
if "ditem" not in st.session_state:
    st.session_state.ditem={
      "Milk":20,
      "Egg":5,
      "Cheese":10,
      "Yougurt":25,
      "Butter":30,
      "Icecream":15
  }
if "gitem" not in st.session_state:
    st.session_state.gitem={
     "Broom":50,
     "Water bottel":10,
     "Waffers/Snacks":20,
     "Cold Drink":25,
     "Stationary":30,
     "Toothpaste":15,
     "Brush":10
  }
if "ftemp" not in st.session_state:
      st.session_state.ftemp={}
if "vtemp" not in st.session_state:
      st.session_state.vtemp={}
if "dtemp" not in st.session_state:
      st.session_state.dtemp={}
if "gtemp" not in st.session_state:
      st.session_state.gtemp={}
st.sidebar.title("Welcome to our Grocery Store")
if "name" not in st.session_state:
    st.session_state.name=" "
if "prize" not in st.session_state:
    st.session_state.prize=[]
st.session_state.name=st.sidebar.text_input("Enter your name")
st.title(f"Greetings to {st.session_state.name}\nWelcome to our Grocery Store")
st.sidebar.success("Following is your Cart")
st.header("Tap the category you want to shop from")
st.sidebar.markdown("### Designed and Developed by Shivam Joshi 💖")
def fruit(ftemp,prize,fitem):
      color=["red","yellow","orange","yellow","violet"]
      img=["https://imgs.search.brave.com/DMMy7WlLowbMi710XL27XA6XyZlsLsbcM3GUB4kkBJk/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly90My5m/dGNkbi5uZXQvanBn/LzA2LzEwLzkxLzg2/LzM2MF9GXzYxMDkx/ODY2MV9FMDhBa0Zs/MGdzeExzVmZKREE1/U0VhNjhZM2F2ZlAy/ZS5qcGc","https://imgs.search.brave.com/M56KoZBlMV_sVtdQ8SbjEiGI0knBQJNiOwt_yon3H4E/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9jZG4u/YnJpdGFubmljYS5j/b20vNDkvMTkyNTQ5/LTA1MC0yREVCMUFB/Mi9idW5jaGVzLW9m/LXllbGxvdy1hbmQt/Z3JlZW4tYmFuYW5h/cy1ob25kdXJhcy5q/cGc_dz00MDAmaD0z/MDAmYz1jcm9w","https://imgs.search.brave.com/f9NJfYxsDwp8quGHjDBzpMNqVvo_egXV5kmW105K9LE/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTEz/MTYwODUzOS9waG90/by9hLWxvdC1vZi1v/cmFuZ2VzLXdpdGgt/c29tZS1jdXQtaW4t/aGFsZi1hbmQtbGVh/dmVzLmpwZz9zPTYx/Mng2MTImdz0wJms9/MjAmYz1xWVVPLW42/VHpFTnJwR1VtY3Bf/bUtiRlpCRHp2OWlL/ZW5rNUpjSm1yQmww/PQ","https://imgs.search.brave.com/s1qZqw7C0fnhUEZQgcaFRuo31b7poO7eqvDC6U06QqM/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly90My5m/dGNkbi5uZXQvanBn/LzE4LzkxLzYzLzc2/LzM2MF9GXzE4OTE2/Mzc2MTdfQXNEUkp2/NDRpRk1zYkZyc3Vl/dmZZUkNza1pwREUy/czEuanBn","https://imgs.search.brave.com/OwShbyBfxm3haU62Lff-BFRs9Ez0S00h1ASFOS-Zvbg/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvOTkz/MTQ0MjEwL3Bob3Rv/L2Fwcmljb3QuanBn/P3M9NjEyeDYxMiZ3/PTAmaz0yMCZjPXVl/QXIzMXl4anNNWDBk/d3ZrMUgycWRUY2pV/UnhtRjVLMjNsVy1L/dWlmeTA9"]
      st.header("Fruits")
      if st.sidebar.button("Tap to CLEAR the Cart"):
          for i in ftemp.keys():
            st.session_state[f"{i}"] = 0
          for i in ftemp.keys():
              ftemp[i]=0
      col1,col2=st.columns([3.5,4])
      with col1:
        for y,i in enumerate(fitem.keys(),start=0):
            st.header(f":{color[y]}[{i}]")
            st.markdown(f"### Price : {fitem[i]} Rs/1 UNIT ")
            st.write("Adjust the quantity you want to purchase")
            ftemp[i]=st.slider(f"How many {i}'s you like to purchase per unit quantity\n(Maximum units at once are 15)",0,15,0,key=f"{i}")
      with col2:
        for i in img:
              st.image(f"{i}\n\n\n\n\n\n\n\n\n")
                
      st.sidebar.markdown(f"## Items in cart of Current category ")
      col1,col2=st.sidebar.columns(2)
      with col1:
            st.warning("       Item")
            for i in ftemp.keys():
                  if ftemp[i]>0:
                        st.markdown(f"### {i} :-")
      with col2:
            st.info("       Quantity")
            for j in ftemp.values():
                  if j>0:
                        st.markdown(f"### {j} (Per 1 unit)  /-")
      st.markdown(f"### :red[To Browse more products scroll up and browse other categories]")

      return ftemp,prize,fitem
def vegies(vtemp,prize,vitem):
      color=["red","violet","green","orange","yellow","blue"]
      img = [
         "https://imgs.search.brave.com/DMEGFktfYxlVjOHH3fBvhPt0uLGxATM_8Jnm2HRTskY/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/ZnJlZS1waG90by9j/bG9zZXVwLWZyZXNo/LXJlZC10b21hdG9l/cy1ibHVlLWRlbmlt/XzE2OTAxNi0yMDc2/Ni5qcGc_c2VtdD1h/aXNfc2VfZW5yaWNo/ZWQmdz03NDAmcT04/MA",
          "https://imgs.search.brave.com/in0pTGHn_o2GypaSYLN-GZqzeo1WC7k_pSfrWUo8Mss/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTcz/NTk3NDkwL3Bob3Rv/L2EtcGlsZS1vZi1y/ZWQtb25pb25zLWFz/LWEtYmFja2dyb3Vu/ZC5qcGc_cz02MTJ4/NjEyJnc9MCZrPTIw/JmM9X09ybk9fRWlr/Vk1YSDRrV0ptM0pP/RmRlUlFoWkR1eVNh/UzNnSG5hWFd3MD0",
          "https://imgs.search.brave.com/Jo9rzDtgnOziri6FdgUGBiLnFhtsJSUHYtsALPtAi_Q/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly90My5m/dGNkbi5uZXQvanBn/LzAxLzM0LzY2LzI4/LzM2MF9GXzEzNDY2/MjgxOF84MWJJV2xQ/T0hVMkl5Q1htWkJU/Mk5oMXZ6UjlYYmtU/YS5qcGc",
          "https://imgs.search.brave.com/lrUHWYAIs-dHnmowSBoMOLgENQX9_GPZuK06R9B6FiI/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9wbHVz/LnVuc3BsYXNoLmNv/bS9wcmVtaXVtX3Bo/b3RvLTE2NjQzNzI1/OTkzNjktZGQ5ZjRl/ZTA3MjU0P2ZtPWpw/ZyZxPTYwJnc9MzAw/MCZhdXRvPWZvcm1h/dCZmaXQ9Y3JvcCZp/eGxpYj1yYi00LjEu/MCZpeGlkPU0zd3hN/akEzZkRCOE1IeHpa/V0Z5WTJoOE1YeDhj/RzkwWVhSdlpYTjha/VzU4TUh4OE1IeDhm/REE9",
          "https://imgs.search.brave.com/pnRKUns-Jozud7cqKFmJfUihU36ikbO92PQTUkjLvqQ/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMudmVjdGVlenku/Y29tL3N5c3RlbS9y/ZXNvdXJjZXMvdGh1/bWJuYWlscy8wMDgv/OTA2LzI5NS9zbWFs/bC9mcmVzaC1nYXJs/aWMtY2xvc2UtdXAt/cGhvdG8uanBn",
          "https://imgs.search.brave.com/BiPEDWlAzCeF_O5jDg_plNpa4iY_bG_VRuDJ8HwEqaE/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9zdGF0/aWMudmVjdGVlenku/Y29tL3N5c3RlbS9y/ZXNvdXJjZXMvdGh1/bWJuYWlscy8wNzQv/NTEwLzEyMC9zbWFs/bC9zcGluYWNoLWxl/YXZlcy1pbi10aGUt/Z2FyZGVuLXBob3Rv/LmpwZw",      ]

      st.header("Vegetables")
      if st.sidebar.button("Tap to CLEAR the Cart"):
          for i in vtemp.keys():
            st.session_state[f"{i}"] = 0
          for i in vtemp.keys():
              vtemp[i]=0
      col1,col2=st.columns([4.5,6.7])
      with col1:
        for y,i in enumerate(vitem.keys(),start=0):
            st.header(f":{color[y]}[{i}]")
            st.markdown(f"### Price : {vitem[i]} Rs/1 UNIT ")
            st.write("Adjust the quantity you want to purchase")
            vtemp[i]=st.slider(f"How many {i}'s you like to purchase per unit quantity\n(Maximum units at once are 15)",0,15,0,key=f"{i}")
            prize.append(vitem[i] * vtemp[i])
      with col2:
        for i in img:
              st.image(f"{i}\n\n\n\n\n\n\n\n\n")
                
      st.sidebar.markdown(f"## Items in cart of Current category ")
      col1,col2=st.sidebar.columns(2)
      with col1:
            st.warning("       Item")
            for i in vtemp.keys():
                  if vtemp[i]>0:
                        st.markdown(f"### {i} :-")
      with col2:
            st.info("       Quantity")
            for j in vtemp.values():
                  if j>0:
                        st.markdown(f"### {j} (Per 1 unit)  /-")
      st.markdown(f"### :green[To Browse more products scroll up and browse other categories]")
      return vtemp,prize,vitem
def dairy(dtemp,prize,ditem):
      color=["white","grey","yellow","orange","yellow","red"]
      img = [
    "https://imgs.search.brave.com/lBhRHWLB9Hv33O-PaEQogIpL-f6KIhxNeN7kavvtFMU/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJjYXZlLmNv/bS93cC93cDIwMzQz/MTEuanBn",

    "https://imgs.search.brave.com/6t6GKm-z1RCUVpngKDqhK-_wTckQ7uHCDNmK-bImzKo/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJhY2Nlc3Mu/Y29tL2Z1bGwvMTQ2/MzUwMC5qcGc",

    "https://imgs.search.brave.com/U3z_dvQcIfMeejqh5LfniRNB8lZiNCaXy_m4F2mvuyA/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMyLmFscGhhY29k/ZXJzLmNvbS8xMjkv/dGh1bWItNDQwLTEy/OTI5MTUud2VicA",

    "https://imgs.search.brave.com/jx00nLxRIJTJiphqYa37FIaXIQz1Ts-SIwLZ583PQw4/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9zdGF0/aWMudmVjdGVlenku/Y29tL3N5c3RlbS9y/ZXNvdXJjZXMvdGh1/bWJuYWlscy8wNDUv/MTcwLzk0MC9zbWFs/bC9jbG9zZS11cC1v/Zi1mcmVzaC15b2d1/cnQtaW4tYS1ib3ds/LW9uLWNvbG9yLWJh/Y2tncm91bmQtcGhv/dG8uanBn",

    "https://imgs.search.brave.com/rktSFtxkYYMN6p1REmleXv7R7pPdk5e-NQtR86SLOSM/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly90My5m/dGNkbi5uZXQvanBn/LzAxLzk4LzQ1Lzky/LzM2MF9GXzE5ODQ1/OTI3OV9abEdkNG9p/SzdFY0lISlFHMXdi/UlEyRE8yQ2FTblJJ/RC5qcGc",
    "https://imgs.search.brave.com/JcH2-EeXt02tdInJn0-f9evjbc1HXa8Xew637-ys08w/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMjE1/Mjg4MjUyNC9waG90/by9tdWx0aWNvbG9y/ZWQtaWNlLWNyZWFt/LWNvbmVzLWFuZC1m/cnVpdHMtc2hvdC1m/cm9tLWFib3ZlLW9u/LWdyYXktYmFja2dy/b3VuZC53ZWJwP2E9/MSZiPTEmcz02MTJ4/NjEyJnc9MCZrPTIw/JmM9N3Fkbllzcy1M/Q3lPcXozbElTelNo/cWFscFA0ajZ4NDZM/bk00eUg4Vksxdz0"]
      st.header("Dairy")
      if st.sidebar.button("Tap to CLEAR the Cart"):
          for i in dtemp.keys():
            st.session_state[f"{i}"] = 0
          for i in dtemp.keys():
              dtemp[i]=0
      col1,col2=st.columns([4.5,6.7])
      with col1:
        for y,i in enumerate(ditem.keys(),start=0):
            if i=="Milk":     
                  st.header(f"{i}")
                  st.markdown(f"### Price : {ditem[i]} Rs/1 LITRE ")
                  st.write("Adjust the quantity you want to purchase")
                  dtemp[i]=st.slider(f"How many {i}'s you like to purchase per unit quantity\n(Maximum units at once are 15)",0,15,0,key=f"{i}")
                  prize.append(ditem[i] * dtemp[i])
            else:
                  st.header(f":{color[y]}[{i}]")
                  st.markdown(f"### Price : {ditem[i]} Rs/1 UNIT ")
                  st.write("Adjust the quantity you want to purchase")
                  st.session_state.dtemp[i]=st.slider(f"How many {i}'s you like to purchase per unit quantity\n(Maximum units at once are 15)",0,15,0,key=f"{i}")
                  prize.append(ditem[i] * dtemp[i])
      with col2:
        for i in img:
              st.image(f"{i}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                
      st.sidebar.markdown(f"## Items in cart of Current category ")
      col1,col2=st.sidebar.columns(2)
      with col1:
            st.warning("       Item")
            for i in dtemp.keys():
                  if dtemp[i]>0:
                        st.markdown(f"### {i} :-")
      with col2:
            st.info("       Quantity")
            for j in dtemp.values():
                  if j>0:
                        st.markdown(f"### {j} (Per 1 unit)  /-")
      st.markdown(f"### :yellow[To Browse more products scroll up and browse other categories]")
      return dtemp,prize,ditem
def general(gtemp,prize,gitem):
      color=["yellow","grey","blue","red","yellow","yellow","green"]
      img = [
   "https://imgs.search.brave.com/I73wYh2-cnQvxsWtNJ9yzrZTaa-5cDeDeZzUn6qWO5o/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/cHJlbWl1bS1waG90/by9yb3ctY29sb3Jm/dWwtYnJvb21zLXNo/b3BfMTI0NzY3MC01/MjE0LmpwZz9zZW10/PWFpc19oeWJyaWQm/dz03NDA",
      "https://imgs.search.brave.com/fH3OR6svLqcnSFOw0Hj6og1LLjnuLIW5kxjzh9AuMVw/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tLm1l/ZGlhLWFtYXpvbi5j/b20vaW1hZ2VzL0kv/NDF0aVN2TFpYWkwu/anBn",

    "https://imgs.search.brave.com/8Oct_KkUYvmsiLAC-kgZcSxQRmbXcm6vTbbbHmSJK3s/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvMTQ3/MTEyMDAxOS9waG90/by9zbmFjay1vbi1k/aXNwbGF5LmpwZz9z/PTYxMng2MTImdz0w/Jms9MjAmYz1XTzIw/NnV1ODlkaFpOWklJ/QWwtU3M0MEZ2M3hY/NGc1cXEybm9BWTlB/Z1pvPQ",
    "https://imgs.search.brave.com/0kf7RWNzrUa6hXHfK3qCt74YQQ9iPX2oKtBSWGfTcqo/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMuaW5kaWFuZXhw/cmVzcy5jb20vMjAx/Ni8xMC9wZXQtYm90/dGxlLmpwZw",
    "https://imgs.search.brave.com/AkxMoyqdj25bE8WCYzXoP6jIDyOqgxQTy7pOo9RjTHM/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvNTIz/ODk4NTQ1L3Bob3Rv/L29mZmljZS1zdXBw/bGllcy5qcGc_cz02/MTJ4NjEyJnc9MCZr/PTIwJmM9dndfU1Z1/czNCU0dDT2Y2ZFNv/c2U2aFBESmFKY3E0/X2ozMDlxa3NNNzJr/Zz0",
    "https://imgs.search.brave.com/VOELEMyzDOXzaz8s5MiaOcj0xfX_u-rBidAgZt748TQ/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93d3cu/bnljY2QuY29tL3dw/LWNvbnRlbnQvdXBs/b2Fkcy8yMDIxLzEw/L1Byb3MtYW5kLUNv/bnMtb2YtRGlmZmVy/ZW50LVR5cGVzLW9m/LVRvb3RocGFzdGUt/NC5qcGc",
    "https://imgs.search.brave.com/3_qX1lXFf_pPhTJzxwH5WIKfCPQC_4UkaRsLN3rObHg/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pbWcu/ZnJlZXBpay5jb20v/cHJlbWl1bS1waG90/by9hcHBseWluZy10/b290aHBhc3RlLXRv/b3RoYnJ1c2gtZGVu/dGFsLWNhcmVfMTk5/NzQzLTEwMjU5Lmpw/Zz9zZW10PWFpc19o/eWJyaWQmdz03NDAm/cT04MA"
]
      st.header("General Items")
      col1,col2=st.columns([4.5,6])
      if st.sidebar.button("Tap to CLEAR the Cart"):
          for i in gtemp.keys():
            st.session_state[f"{i}"] = 0
          for i in gtemp.keys():
              gtemp[i]=0
      with col1:
        for y,i in enumerate(gitem.keys(),start=0):
            st.header(f":{color[y]}[{i}]")
            st.markdown(f"### Price : {gitem[i]} Rs/1 UNIT ")
            st.write("Adjust the quantity you want to purchase")
            gtemp[i]=st.slider(f"How many {i}'s you like to purchase per unit quantity\n(Maximum units at once are 15)",0,15,0,key=f"{i}")
      with col2:
        for i in img:
              st.image(f"{i}\n\n\n\n\n\n\n\n\n\n\n\n")
                
      st.sidebar.markdown(f"## Items in cart of Current category ")
      col1,col2=st.sidebar.columns(2)
      with col1:
            st.warning("       Item")
            for i in gtemp.keys():
                  if gtemp[i]>0:
                        st.markdown(f"### {i} :-")
      with col2:
            st.info("       Quantity")
            for j in gtemp.values():
                  if j>0:
                        st.markdown(f"### {j} (Per 1 unit)  /-")
      st.markdown(f"### :blue[To Browse more products scroll up and browse other categories]")
      return gtemp,prize,gitem
@st.dialog("Billing Section")
def checkout(ftemp,vtemp,dtemp,gtemp,name,gitem,fitem,vitem,ditem):
      now=dt.datetime.now()
      time=now.strftime("%I,%M,%S,%p")
      st.balloons()
      st.snow()
      total=0
      prize=[]
      if "cart" not in st.session_state:
            st.session_state.cart={}
      for i,j in ftemp.items():
            if j>0:
                  st.session_state.cart[i]=st.session_state.ftemp[i]
                  total+=(st.session_state.ftemp[i])*(st.session_state.fitem[i])
      for i,j in vtemp.items():
            if j>0:
                  st.session_state.cart[i]=st.session_state.vtemp[i]
                  total += st.session_state.vitem[i]*st.session_state.vtemp[i]
      for i,j in dtemp.items():
            if j>0:
                  st.session_state.cart[i]=st.session_state.dtemp[i]
                  total += st.session_state.ditem[i]*st.session_state.dtemp[i]
      for i,j in gtemp.items():
            if j>0:
                  st.session_state.cart[i]=st.session_state.gtemp[i]
                  total += st.session_state.gitem[i]*st.session_state.gtemp[i]
      for i,j in st.session_state.cart.items():
            st.markdown(f"### {i} : {j} (Per 1 unit)  /-")
      for i in st.session_state.cart.keys():
          if i in st.session_state.fitem.keys():
              prize.append(st.session_state.fitem[i])
      for i in st.session_state.cart.keys():
          if i in st.session_state.vitem.keys():
              prize.append(st.session_state.vitem[i])
      for i in st.session_state.cart.keys():
          if i in st.session_state.ditem.keys():
              prize.append(st.session_state.ditem[i])
      for i in st.session_state.cart.keys():
          if i in st.session_state.gitem.keys():
              prize.append(st.session_state.gitem[i])
      if len(st.session_state.cart)==0:
          st.warning("Cart is empty mate GO Shop")
      else:
          pdf = FPDF()
          pdf.add_page()

          # Header
          pdf.set_font("Arial", "B", 24)
          pdf.cell(0, 15, "SHIVAM'S FRESH CART", ln=1, align="C")

          pdf.set_font("Arial", "", 12)
          pdf.cell(0, 8, "Thank You For Shopping With Us", ln=1, align="C")

          pdf.ln(5)

          # Customer Details
          pdf.set_font("Arial", "B", 12)
          pdf.cell(50, 8, f"Customer : {st.session_state.name}", ln=1)
          pdf.cell(50, 8, f"Date : {now.strftime('%d-%m-%Y')}", ln=1)
          pdf.cell(50, 8, f"Time : {time}", ln=1)

          billno = rd.randint(1000, 10000)
          pdf.cell(50, 8, f"Bill No : {billno}", ln=1)

          pdf.ln(5)

          # Table Header (Adding the Price Column!)
          pdf.set_font("Arial", "B", 14)
          pdf.cell(90, 10, "Item", border=1, ln=0, align="L")
          pdf.cell(50, 10, "Price (Rs)", border=1, ln=0, align="C")
          pdf.cell(50, 10, "Quantity", border=1, ln=1, align="C")

          # Items (YOUR exact logic, using your 'prize' list)
          pdf.set_font("Arial", "", 12)

          idx = 0
          for i, j in st.session_state.cart.items():
              current_prize = prize[idx]
              pdf.cell(90, 10, txt=f"{i}", border=1, ln=0, align="L")
              pdf.cell(50, 10, txt=f"{current_prize}", border=1, ln=0, align="C")
              pdf.cell(50, 10, txt=f"{j}", border=1, ln=1, align="C")
              idx += 1

          pdf.ln(10)

          # Total
          pdf.set_font("Arial", "B", 16)
          pdf.cell(0, 10, f"Grand Total : Rs {total}", ln=1, align="R")

          pdf.ln(15)

          # Footer & Signature
          pdf.set_font("Arial", "I", 12)
          pdf.cell(0, 8, "Warm Regards! Do visit us again :)", ln=1, align="C")

          pdf.ln(2)
          pdf.set_font("Arial", "B", 10)
          pdf.cell(0, 8, "Designed and engineered by Shivam Joshi <3", ln=1, align="C")

          pdf.output("bill.pdf")
          with open("bill.pdf", "rb") as file:
              st.download_button("Click to download bill", file, file_name="bill.pdf", mime="application/pdf")


      
      
            
if "cat" not in st.session_state:
      st.session_state.cat=" "              
col1,col2,col3,col4=st.columns(4)
with col1:
  st.success("Fruits")
  st.image("https://imgs.search.brave.com/DMMy7WlLowbMi710XL27XA6XyZlsLsbcM3GUB4kkBJk/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly90My5m/dGNkbi5uZXQvanBn/LzA2LzEwLzkxLzg2/LzM2MF9GXzYxMDkx/ODY2MV9FMDhBa0Zs/MGdzeExzVmZKREE1/U0VhNjhZM2F2ZlAy/ZS5qcGc")
  if st.button("Tap to browse fruits"):
    st.session_state.cat="fruit"    
    st.session_state["fruit"]=True
with col2:
  st.info("Vegetables")
  st.write("\n\n")
  st.image("https://imgs.search.brave.com/aXUAwxZ6NYA2AkgcBezpGprrsf7hK4OAPjFYFwoOIBU/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93YWxs/cGFwZXJjYXZlLmNv/bS93cC93cDEyNjQ5/NDMyLmpwZw")
  if st.button("Browse vegetables"):
      st.session_state.cat="vegies"
      st.session_state["vegies"]=True  
    
with col3:
  st.error("Dairy")
  st.image("https://imgs.search.brave.com/Wq_BGmHYeNVPdIU5tIo4Zww-8jXthyJupR0l3bHZRPU/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93MC5w/ZWFrcHguY29tL3dh/bGxwYXBlci8yMjYv/OTk1L0hELXdhbGxw/YXBlci1kYWlyeS1w/cm9kdWN0cy1kZWxp/Y2lvdXMtZm9vZC1m/cnVpdC1ncmFwZS1j/aGVlc2Utc3BpY2Ut/bWlsay1nYXJsaWMt/dmVnZXRhYmxlcy1j/cmVhbS10aHVtYm5h/aWwuanBn")
  if st.button("Browse dairy products"):
      st.session_state.cat="dairy"
      st.session_state["dairy"]=True
with col4:
  st.warning("General Stuff")
  st.image("https://imgs.search.brave.com/BFzP3u-hNwXNQ0EACrnjXY5k1LRdNrdGyd4R4PKyG_k/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9zdGF0/aWMudmVjdGVlenku/Y29tL3N5c3RlbS9y/ZXNvdXJjZXMvdGh1/bWJuYWlscy8wMjcv/MzkxLzU3Ni9zbWFs/bC9jaGVhcC1wbGFz/dGljLWhvdXNlaG9s/ZC1pdGVtcy1mb3It/c2FsZS1vbi10aGUt/bWFya2V0LWNsb3Nl/LXVwLWZyZWUtcGhv/dG8uanBn")
  if st.button("Browse general items"):
        st.session_state.cat="general"
        st.session_state["general"]=True  
  st.write("\n\n")
if st.session_state.get(st.session_state.cat):
      if st.session_state.cat=="fruit":
            fruit(st.session_state.ftemp,st.session_state.prize,st.session_state.fitem)
      elif st.session_state.cat=="vegies":
            vegies(st.session_state.vtemp,st.session_state.prize,st.session_state.vitem)
      elif st.session_state.cat=="dairy":
            dairy(st.session_state.dtemp,st.session_state.prize,st.session_state.ditem)
      elif st.session_state.cat=="general":
            general(st.session_state.gtemp,st.session_state.prize,st.session_state.gitem)
if st.sidebar.button("Checkout"):
    checkout(st.session_state.ftemp, st.session_state.vtemp, st.session_state.dtemp, st.session_state.gtemp,
             st.session_state.name,st.session_state.gitem,st.session_state.fitem, st.session_state.vitem, st.session_state.ditem)
    