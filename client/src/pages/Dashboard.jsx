import { useState, useEffect } from 'react'
import { toast } from 'react-toastify'
import { useNavigate } from 'react-router-dom'
import { FaSignInAlt } from 'react-icons/fa'
import { useSelector, useDispatch } from 'react-redux'
import { login, reset } from '../features/auth/authSlice'
import Spinner from '../components/Spinner'

function Dashboard() {

  return (
    <>
      <section className='heading'>
        <h1>
          <FaSignInAlt /> Login
        </h1>
        <p>Dashboard Page</p>
      </section>
    </>
  )
}

export default Dashboard
