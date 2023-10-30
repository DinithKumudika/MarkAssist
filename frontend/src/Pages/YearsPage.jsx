import NavBar from '../Components/NavBar'
import SideBar from '../Components/SideBar'
import Years from '../Components/Years'
import { useParams, useNavigate } from 'react-router-dom'
import {useEffect, useState} from 'react'
import axios from 'axios'
function YearsPage() {
  const { subjectCode } = useParams()
  const allItems=JSON.parse(localStorage.getItem('tokenData'));
  const accessToken = localStorage.getItem('accessToken')
  if(!allItems){
    window.location.href="/";
  }
  const user_id=allItems['user_id'];
  const userType = allItems['user_role'];
  const [isClicked,setClick] = useState("inner");
  const [years,setYears] = useState([]);
  useEffect(()=>{
    fetchYears();
  },[]);

  const fetchYears = async () =>{
      const headers = {
        Authorization: `Bearer ${accessToken}`,
      };
      console.log("HEADERS::::"+subjectCode,user_id);
      if(userType==='teacher'){
        axios
        .get(`http://127.0.0.1:8000/api_v1/subjects/years/user/${user_id}/${subjectCode}`)
        .then((response) => {
          const data = response.data;
          setYears(data);
        })
        .catch((error) => {
          console.error(error);
        });
      }else if(userType==='admin'){
        axios
        .get(`http://127.0.0.1:8000/api_v1/subjects/years/${subjectCode}`)
        .then((response) => {
          const data = response.data;
          setYears(data);
        })
        .catch((error) => {
          console.error(error);
        });
      }
  }

  //Function to handle the click of the hamburger menu
  const handleClick = () => {
    if(isClicked==="outer"){
    setClick("inner")
    }else{
    setClick("outer")
    }
    // console.log(isClicked)
  }

  return (
    <div>
      <NavBar black clicked={isClicked} />
      <SideBar mcq subjects markingSchemes answerPapers clicked={isClicked} onClickFunc={handleClick}/>
      <Years clicked={isClicked} data={years}/>
    </div>
  )
}

export default YearsPage
