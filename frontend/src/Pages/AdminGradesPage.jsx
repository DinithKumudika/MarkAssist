import React from 'react'
import NavBar from '../Components/NavBar'
import SideBar from '../Components/SideBar'
import {useState} from 'react'
import AdminDashboard from '../Components/Dashboards/AdminDashboard'
import AdminGrade from '../Components/AdminGrade'
function AdminGradesPage() {

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
      <AdminGrade clicked={isClicked}/>
      {/* <Subjects clicked={isClicked}/> */}
    </div>
  )
}

export default AdminGradesPage
