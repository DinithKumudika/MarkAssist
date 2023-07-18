import classnames from 'classnames';
import SubjectBox from './SubjectBox';
import {Link, useLocation} from 'react-router-dom';
import {useState, useEffect} from 'react';
import SubjectAddBox from './SubjectAddBox';
import Button from '../Button';
import { useSort } from '../../Hooks/Sort';
import axios from 'axios';
function Subjects({clicked,data}) {
  const length = data.length;
  const allItems=JSON.parse(localStorage.getItem('tokenData'));
  console.log("DATA:",data);
  if(!allItems){
    window.location.href="/";
  }
  const userType = allItems['user_role'];

  const classes = classnames('sidebar static max-sm:ml-16');

  const location = useLocation();
  const pathName = location.pathname.split('/').filter((path) => path !== '')
  // console.log(pathName[0]);

  //Modal show unshow
  const [show, setShow] = useState(false);
  //Sort setvalue
  // let sortedData=data
  const [sort,setSort] = useState("")
  const [sorteddata,setsorteddata] = useState(data)
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
    // console.log(formData);
    const sortedData = [...data].sort((a, b) => `${a}.${event.target.value}`.localeCompare(`${b}.${event.target.value}`));
    // console.log("sortedData::",sortedData,event.target.value)
    setsorteddata(sortedData)
  }
  // sortedData = useSort(data,sort,"asc")

  useEffect(()=>{
    // Get all the teachers list
    axios
    .get(`http://127.0.0.1:8000/api_v1/admins/teachers`)
    .then((response) => {
      const data = response.data
      setTeachers(data)
      console.log("Teachers:",data)
      // Process the response data or update your React component state
    })
  },[])

  const subjects = (sorteddata).map((subject,index)=>{
    // console.log(subject);
    return <Link key={index} to={"/"+pathName[0]+"/years/"+subject.subjectCode} className='h-24'><SubjectBox onClick={handleClick} key={index} subjectCode={subject.subjectCode} subjectName={subject.subjectName} userType={userType}/></Link>
  })

  return (
    <div className={`${classes} ${clicked === 'outer' ? ' ml-16 outer w-[calc(100vw-64px)]' : 'ml-64 w-[calc(100vw-256px)] inner'} max-sm:16 max-sm:w-[calc(100vw-64px)]`}>
      <div className='flex justify-center items-center sidebar'>
          <div className='mt-[8%] h-[85%] w-11/12'>
            <div className='flex flex-row justify-between items-center mb-4'>
              <div className='flex flex-row items-center justify-start h-10'>
                  <p className='p-2 rounded rounded-lg w-20 mr-4 font-bold text-[#191854]'>Subjects({length})</p>
                  <p className='p-2 rounded rounded-lg w-20 '>Sort by:</p>
                  <select className='w-28 'name='sort' value={sort} onChange={handleSortChange}>
                    <option value="subjectName" className='font-bold'>Name</option>
                    <option value="subjectCode" className='font-bold'>Subject Code</option>
                  </select>
                  {/* <p className='bg-black/20 p-2 rounded rounded-lg'>Grade</p> */}
              </div>
              { userType === "admin" &&
                <Button onClick={handleClick}> Add a Subject</Button>
              }
            </div>
            <div className='h-custom-94% py-2 flex flex-wrap overflow-auto'>
              {subjects}
            </div>
          </div>
      </div>
      {show && <SubjectAddBox closeFunc={closeModal} teachers={teachers}/>}
    </div>
  )
}

export default Subjects
