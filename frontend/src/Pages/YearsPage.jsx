import NavBar from '../Components/NavBar'
import SideBar from '../Components/SideBar'
import Years from '../Components/Years'

import { useParams, useNavigate } from 'react-router-dom'
import {useEffect, useState} from 'react'
import axios from 'axios'
function YearsPage() {
  const { subjectCode } = useParams()
  const allItems=JSON.parse(localStorage.getItem('token'));
  if(!allItems){
    window.location.href="/";
  }
  const user_id=allItems['user_id'];
  const [isClicked,setClick] = useState("outer");
  const [years,setYears] = useState([]);

  useEffect(()=>{
    fetchYears();
  },[]);

  const fetchYears = async () =>{
    try{
      const config = {
        headers: {
          Authorization: `Bearer ${allItems['token']}`,
        },
      }
      const response = await axios.get(`http://localhost:5000/api_v1/subjects/years/${user_id}/${subjectCode}`,config);
      const data = response.data;
      setYears(data);
    }catch(error){
      console.log(error);
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
      <NavBar black />
      <SideBar mcq subjects markingSchemes answerPapers clicked={isClicked} onClickFunc={handleClick}/>
      <Years clicked={isClicked} data={years}/>
    </div>
  )
}

export default YearsPage
