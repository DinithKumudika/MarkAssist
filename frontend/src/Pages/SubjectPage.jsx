import { useParams, useNavigate } from 'react-router-dom'
function SubjectPage() {

  const { subjectId } = useParams()
  return (
    <div>
      {subjectId}
    </div>
  )
}

export default SubjectPage
