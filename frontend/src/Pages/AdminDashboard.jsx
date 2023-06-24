import React from 'react'
import NavBar from '../Components/NavBar'
import SideBar from '../Components/SideBar'
import Subjects from '../Components/Subjects/Subjects'
import {useState} from 'react'
function AdminDashboard() {

  const [isClicked,setClick] = useState("outer")

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
      <NavBar />
      <SideBar dashboard subjects clicked={isClicked} onClickFunc={handleClick}/>
      {/* <Subjects clicked={isClicked}/> */}
    </div>
  )
}

export default AdminDashboard
