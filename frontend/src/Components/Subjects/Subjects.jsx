import classnames from 'classnames';
import SubjectBox from './SubjectBox';
import {Link, useLocation} from 'react-router-dom';
import {useState, useEffect} from 'react';
import SubjectAddBox from './SubjectAddBox';
import Button from '../Button';
import { useSort } from '../../Hooks/Sort';
import axios from 'axios';
import BreadCrumb from '../BreadCrumb';
function Subjects({clicked,data}) {
  const length = data?.length;
  console.log("Length:",length);
  const allItems=JSON.parse(localStorage.getItem('tokenData'));
  console.log("DATA:",data);
  if(!allItems){
    window.location.href="/";
  }
  const userType = allItems['user_role'];

  const classes = classnames('sidebar absolute top-[52px] max-sm:pl-16 bg-background overflow-auto pt-6 pb-[60px] ');

  const location = useLocation();
  const pathName = location.pathname.split('/').filter((path) => path !== '')
  // console.log(pathName[0]);

  //Modal show unshow
  const [show, setShow] = useState(false);
  //Sort setvalue
  // let sortedData=data
  const [sort,setSort] = useState("subjectName")
  const [sorteddata,setsorteddata] = useState(data ? data : null)
  // console.log("sorteddata",sorteddata)
  //To save teachers list
  const [teachers,setTeachers] = useState([]);
  //Modal show unshow function
  const handleClick = (e) => {
    e.preventDefault();
    setShow((prev)=>!prev);
    // console.log(show);
  }
  const closeModal = () =>{
    setShow(false);
  }

  //Sort select change
  const handleSortChange = (event) =>{
    setSort(event.target.value)
    console.log("sort::",event.target.value);
    if(event.target.value==="subjectName-ASC"){
      const sortedData = [...data].sort((a, b) => a.subjectName.localeCompare(b.subjectName));
      console.log("sortedData::",sortedData)
      setsorteddata(sortedData)
    }else if(event.target.value==="subjectCode-ASC"){
      const sortedData = [...data].sort((a, b) => a.subjectCode.localeCompare(b.subjectCode));
      console.log("sortedData::",sortedData)
      setsorteddata(sortedData)
    }else if(event.target.value==="subjectName-DSC"){
      const sortedData = [...data].sort((a, b) => a.subjectCode.localeCompare(b.subjectCode)*-1);
      console.log("sortedData::",sortedData)
      setsorteddata(sortedData)
    }else if(event.target.value==="subjectCode-DSC"){
      const sortedData = [...data].sort((a, b) => a.subjectCode.localeCompare(b.subjectCode)*-1);
      console.log("sortedData::",sortedData)
      setsorteddata(sortedData)
    }
    // const sortedData = [...data].sort((a, b) =>`${a}.${event.target.value}`.localeCompare(`${b}.${event.target.value}`));
    // console.log("sortedData::",sortedData)
  }
  // sortedData = useSort(data,sort,"asc")

  useEffect(()=>{
    // Get all the teachers list
    axios
    .get(`/admins/teachers`)
    .then((response) => {
      const data = response.data
      setTeachers(data)
      console.log("Teachers:",data)
      // Process the response data or update your React component state
    })
  },[])

  const subjects = (sorteddata)?.map((subject,index)=>{
    // console.log(subject);
    return <Link key={index} to={"/"+pathName[0]+"/years/"+subject?.subjectCode} className='h-40 w-full'><SubjectBox onClick={handleClick} key={index} subject={subject} backgroundUrl={subject.backgroundImage} subjectCode={subject.subjectCode} subjectName={subject.subjectName} userType={userType}/></Link>
  })

  return (
    <div className={`${classes} ${clicked === 'outer' ? ' pl-16 outer ' : 'pl-64 inner'} max-sm:pl-16 w-full`}>
      <div className='flex flex-col justify-center items-center sidebar overflow-hidden h-fit'>
          <div className='w-11/12'>
            <BreadCrumb/>
          </div>
          <div className='bg-white p-4 rounded w-11/12 min-h-max '>
            <div className='flex flex-row justify-between items-center mb-4 min-h-max'>
              <div className='flex flex-row items-center justify-start h-10'>
                  <p className='p-2 rounded rounded-lg w-20 mr-4 font-bold text-[#191854]'>Subjects({length})</p>
                  <p className='p-2 rounded rounded-lg w-20 '>Sort by:</p>
                  <select className='w-28 hover:cursor-pointer 'name='sort' value={sort} onChange={handleSortChange}>
                    <option value="subjectName-ASC" className='hover:cursor-pointer font-bold'>Name-ASC</option>
                    <option value="subjectName-DSC" className='hover:cursor-pointer font-bold'>Name-DSC</option>
                    <option value="subjectCode-ASC" className='hover:cursor-pointer font-bold'>Subject Code-ASC</option>
                    <option value="subjectCode-DSC" className='hover:cursor-pointer font-bold'>Subject Code-DSC</option>
                  </select>
                  {/* <p className='bg-black/20 p-2 rounded rounded-lg'>Grade</p> */}
              </div>
              { userType === "admin" &&
                <Button onClick={handleClick}> Add a Subject</Button>
              }
            </div>
            <div className='grid lg:grid-cols-3 md:grid-cols-2 grid-cols-1 gap-6'>
              {subjects}
              {subjects}
            </div>
          </div>
      </div>
      {show && <SubjectAddBox closeFunc={closeModal} teachers={teachers}/>}
    </div>
  )
}

export default Subjects
