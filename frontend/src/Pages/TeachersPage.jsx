import NavBar from '../Components/NavBar'
import SideBar from '../Components/SideBar'
import Teachers from '../Components/Teachers'
import {useEffect, useState} from 'react'
import axios from 'axios'
function TeachersPage() {
  const allItems=JSON.parse(localStorage.getItem('tokenData'));
  if(!allItems){
    window.location.href="/";
  }
  const user_id=allItems['user_id'];
  const userType = allItems['user_role'];
  const [isClicked,setClick] = useState("inner");
  const [teachers,setTeachers] = useState([]);

  useEffect(()=>{
    fetchTeachers();
  },[]);

  const fetchTeachers = async () =>{
    try{
      const config = {
        headers: {
          Authorization: `Bearer ${allItems['tokenData']}`,
        },
      }
      //****Methana subjects code eken group karaganna oona
      const response = await axios.get(`http://127.0.0.1:8000/api_v1/admins/teachers`);
      const data = response.data;
      setTeachers(data);
    }catch(error){
      console.log(error);
    }
  }
  // console.log(teachers);
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
      <NavBar black onClickFunc={handleClick} clicked={isClicked}/>
      <SideBar mcq subjects markingSchemes answerPapers clicked={isClicked} onClickFunc={handleClick}/>
      <Teachers clicked={isClicked} data={teachers}/>
    </div>
  )
}

export default TeachersPage