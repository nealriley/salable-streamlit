import streamlit as st
import streamlit.components.v1 as components  # Import Streamlit
import uuid
import time
from utils import check_grantee_id

st.title("Welcome to Buttons for Teams!")

BALLOON_PLAN="4200f175-0156-4b29-a45e-68c176608e04"
SPINNER_PLAN="a9c9b8d7-ed78-47dc-a888-639a0d5e6ca3"
TEAM_PLAN="ab044b87-9d97-47c5-820f-f53f77ed8fa4"

if "capabilities" not in st.session_state:
    st.session_state["capabilities"]=""
params=st.experimental_get_query_params()
if 'grantee_id' not in st.session_state:
    if "grantee_id" not in params:
      myuuid = uuid.uuid4()    
      st.session_state['grantee_id'] = str(myuuid)
    else: 
      st.session_state['grantee_id'] = params['grantee_id'][0]
if 'team_grantee_id' not in st.session_state:
    myuuid = uuid.uuid4()    
    st.session_state['team_grantee_id'] = str(myuuid)
result = check_grantee_id(",".join([st.session_state['team_grantee_id'], st.session_state['grantee_id']]))
if (result['status']==204):
    st.session_state['capabilities'] = ""
else:
    st.session_state['capabilities'] = ",".join(result['data']['capabilities'])

st.write("### We offer 3 awesome features")
st.write("You can use our three button in different ways. You can either buy Spinners or Balloons for yourself, or you can buy Spinners, Balloons (And Pings included!) for your team.")

col1, col2, col3= st.columns(3)
with col1:
    st.header("Spinners!")
    if 'can_use_spinner' in st.session_state['capabilities'].split(','):
        if st.button("Spin Away"):
            with st.spinner('Wait for it...'):
                time.sleep(2)
    else: 
        st.warning('Please purchase a team or user license', icon="⚠️")
with col2:
    st.header("Balloons!")
    if 'can_use_balloon' in st.session_state['capabilities'].split(','):
        if st.button("Make Balloons"):
            st.balloons()
    else: 
        st.warning('Please purchase a team or user license', icon="⚠️")
with col3:
    st.header("Pings!")
    if 'can_use_ping' in st.session_state['capabilities'].split(','):
        if st.button('Three cheers'):
            st.toast('Hip!')
            time.sleep(.5)
            st.toast('Hip!')
            time.sleep(.5)
            st.toast('Hooray!', icon='🎉')
    else: 
        st.warning('Please purchase a team license', icon="⚠️")
st.markdown("""---""") 

st.header("Purchase a license")

col1, col2 = st.columns(2)
st.header("User")
selection=st.text_input(value=st.session_state["grantee_id"], label="UserID")
if st.button("Try a New User"):
    myuuid = uuid.uuid4()    
    st.session_state['grantee_id'] = str(myuuid)
    st.experimental_rerun()


# Render the h1 block, contained in a frame of size 200x200.
components.html("""
<div id="pricing-table"></div>
<script type="module">
  import {SalablePricingTable} from "https://cdn.salable.app/latest/index.js"
  (async () => {
    const salable = new SalablePricingTable(
      {
        pricingTableNode: document.querySelector('#pricing-table'),
        pricingTableUuid: '079d839c-4628-4428-aa1d-bce481b124ac',
        apiKey: 'test_38d98b4e2ea3c642ad7db33884c1a5831a8491da',
        globalPlanOptions: {
          granteeId: '%s',
          successUrl: '%s?grantee_id=%s',
          cancelUrl: '%s?grantee_id=%s'
        },
        theme: 'light'
      },
      {
        member: '%s',
        customer: {
          email: ""
        }
      }
    );
    await salable.init();
    const links = document.querySelectorAll('a[target="_top"]');
    links.forEach(link => {
        link.setAttribute('target', '_new');
    });
  })();
</script>
""" % (st.session_state['grantee_id'], 
      'https://build-your-businsess.streamlit.app//Super_Awesome_Buttons_Demo',st.session_state['grantee_id'], 
      'https://build-your-businsess.streamlit.app//Super_Awesome_Buttons_Demo', st.session_state['grantee_id'], 
      st.session_state['grantee_id']), width=600, height=500)

st.markdown("---")
st.header("Team")
teamselection=st.text_input(value=st.session_state["team_grantee_id"],label="TeamID")
if st.button("Try a New Team"):
    myuuid = uuid.uuid4()    
    st.session_state['team_grantee_id'] = str(myuuid)
    st.experimental_rerun()
# Render the h1 block, contained in a frame of size 200x200.
components.html("""
<div id="pricing-table-team"></div>
<script type="module">
  import {SalablePricingTable} from "https://cdn.salable.app/latest/index.js"
  (async () => {
    const salable = new SalablePricingTable(
      {
        pricingTableNode: document.querySelector('#pricing-table-team'),
        pricingTableUuid: 'a14c3f9c-2a07-4bb9-9bd9-d3f19c91bcbd',
        apiKey: 'test_38d98b4e2ea3c642ad7db33884c1a5831a8491da',
        globalPlanOptions: {
          granteeId: '%s',
          successUrl: '%s?grantee_id=%s',
          cancelUrl: '%s?grantee_id=%s'
        },
        theme: 'light'
      },
      {
        member: '%s',
        customer: {
          email: ""
        }
      }
    );
    await salable.init();
    const links = document.querySelectorAll('a[target="_top"]');
    links.forEach(link => {
        link.setAttribute('target', '_new');
    });
  })();
</script>
""" % (st.session_state['grantee_id'], 
      'https://build-your-businsess.streamlit.app//Super_Awesome_Buttons_Demo',st.session_state['team_grantee_id'], 
      'https://build-your-businsess.streamlit.app//Super_Awesome_Buttons_Demo', st.session_state['team_grantee_id'], 
      st.session_state['grantee_id']), width=600, height=500)
with st.sidebar:
    st.write(f"""
    
    UserID: {st.session_state["grantee_id"]} 
    
    Capabilities: {st.session_state["capabilities"]}""") 
