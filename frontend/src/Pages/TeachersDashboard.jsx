import React from 'react'
import NavBar from '../Components/NavBar'
import SideBar from '../Components/SideBar'
import TeacherDashboard from '../Components/Dashboards/TeacherDashboard'
import Subjects from '../Components/Subjects/Subjects'
import {useState} from 'react'
function TeachersDashboard() {

  const [isClicked,setClick] = useState("inner")

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
      <NavBar clicked={isClicked}/>
      <SideBar dashboard subjects clicked={isClicked} onClickFunc={handleClick}/>
      <TeacherDashboard clicked={isClicked}/>
      {/* <Subjects clicked={isClicked}/> */}
    </div>
  )
}

export default TeachersDashboard
