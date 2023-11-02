import React from 'react'
import Table1 from '../Components/Table1'
import TeachersAdd from '../Components/TeachersAdd'
import test1 from '../Components/test1'
import Test2 from '../Components/Test2'

function TeacherPage() {
  return (
    <div>
      {/* <TeachersAdd /> */}
      <div className="flex flex-col mt-20 space-y-0">
      <Test2 />
      <Table1 />
      </div>
    </div>
  )
}

export default TeacherPage
