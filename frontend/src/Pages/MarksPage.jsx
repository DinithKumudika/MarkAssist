import NavBar from '../Components/NavBar'
import SideBar from '../Components/SideBar'
import Marks from '../Components/Marks/Marks'
import {useEffect, useState} from 'react'
import {useParams} from 'react-router-dom'
import axios from 'axios'
function MarksPage() {
  const allItems=JSON.parse(localStorage.getItem('tokenData'));
  console.log(allItems);
  if(!allItems){
    window.location.href="/";
  }
  const user_id=allItems['user_id'];
  const [isClicked,setClick] = useState("outer");
  const [markingScheme,setMarkingScheme] = useState([]);

  const handleClick = () => {
    if(isClicked==="outer"){
    setClick("inner")
    // console.log(isClicked)
    }else{
    setClick("outer")
    // console.log(isClicked)
    }
  }
  return (
    <div>
      <NavBar />
      <SideBar mcq subjects markingSchemes answerPapers clicked={isClicked} onClickFunc={handleClick}/>
      <Marks clicked={isClicked} data="hello"/>
    </div>
  )
}

export default MarksPage
