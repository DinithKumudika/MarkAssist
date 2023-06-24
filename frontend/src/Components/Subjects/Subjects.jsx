import classnames from 'classnames';
import SubjectBox from './SubjectBox';
import {Link, useLocation} from 'react-router-dom';
function Subjects({clicked,data}) {
  const classes = classnames('sidebar static max-sm:ml-16');

  const location = useLocation();
  const pathName = location.pathname.split('/').filter((path) => path !== '')
  // console.log(pathName[0]);
  const subjects = data.map((subject,index)=>{
    // console.log(subject);
    return <Link key={index} to={"/"+pathName[0]+"/years/"+subject.subjectCode}><SubjectBox key={index} subjectCode={subject.subjectCode} subjectName={subject.subjectName}/></Link>
  })

  return (
    <div className={`${classes} ${clicked === 'outer' ? 'ml-16 outer' : 'ml-64 inner'}`}>
      <div className='flex justify-center items-center sidebar'>
          <div className='mt-[8%] h-[85%] w-11/12'>
            <div className='flex flex-row items-center justify-between px-10 h-10 mb-4'>
                <p className='bg-black/20 p-2 rounded rounded-lg'>Acdemic year</p>
                <p className='bg-black/20 p-2 rounded rounded-lg'>Grade</p>
            </div>
            
            <div className='h-custom-94% py-2 flex flex-wrap overflow-auto'>
              {subjects}
            </div>
          </div>
      </div>
    </div>
  )
}

export default Subjects
