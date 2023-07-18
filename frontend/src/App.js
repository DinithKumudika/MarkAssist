import { Route, Routes } from 'react-router-dom';
import EssayPage from './Pages/EssayPage';
import Login from './Pages/Login';
import Register from './Pages/Register';
import EmailVerifiedPage from './Pages/EmailVerifiedPage';
import TeacherPasswordChangePage from './Pages/TeacherPasswordChangePage';
import AdminDashboard from './Pages/AdminDashboard';
import SubjectsPage from './Pages/SubjectsPage';
import SubjectPage from './Pages/SubjectPage';
import YearsPage from './Pages/YearsPage';
import MarkingSchemesPage from './Pages/MarkingSchemesPage';
import MarkingSchemeConfigurePage from './Pages/MarkingSchemeConfigurePage';
import AnswerSheetsPage from './Pages/AnswerSheetsPage';
import TopBar from './Components/TopBar';
import TeachersPage from './Pages/TeachersPage';
import MarksPage from './Pages/MarksPage';
import PapersPage from './Pages/PapersPage';
import './Components/TopBar.css';

function App(){
  return(
    <div className='h-full'>
      {/* <TopBar /> */}
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        {/* <Route path="/dashboard" element={<Dashboard />} /> */}
        <Route path="/verify_account" element={<TeacherPasswordChangePage />} />
        <Route path="/email_verified" element={<EmailVerifiedPage />} />

        <Route path="/essayPage" element={<EssayPage />} />

        <Route path="/subjects" element={<SubjectsPage />} />
        <Route path="/subjects/:subjectId" element={<SubjectPage />} />
        <Route path="/subjects/years/:subjectCode" element={<YearsPage />} />
        <Route path="/subjects/:year/:subjectId" element={<PapersPage />} />


        <Route path="/markingschemes" element={<SubjectsPage />} />
        <Route path="/markingschemes/years/:subjectCode" element={<YearsPage />} />
        <Route path="/markingschemes/:year/:subjectId" element={<MarkingSchemesPage />} />
         {/* <Route path="/markingschemes/:markingschemeId/:subjectId" element={<MarkingSchemeConfigurePage />} /> */}
         <Route path="/markingschemes/:subjectId" element={<MarkingSchemeConfigurePage />} />

        <Route path="/answersheets" element={<SubjectsPage />} />
        <Route path="/answersheets/years/:subjectCode" element={<YearsPage />} />
        <Route path="/answersheets/:year/:subjectId" element={<AnswerSheetsPage />} />
        <Route path="/answersheets/marks/:year/:subjectId/:paperId" element={<MarksPage />} />

        
        <Route path="/admin/dashboard" element={<AdminDashboard />} />
        <Route path="/admin/teachers" element={<TeachersPage />} />


      </Routes>
    </div>
  );
}

export default App;
