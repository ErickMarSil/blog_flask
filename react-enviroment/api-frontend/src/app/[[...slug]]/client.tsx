import dynamic from 'next/dynamic'
import React from 'react'
 
const App = dynamic(() => import('../../pages/Login/mainApp/App'), { ssr: false })
 
export function ClientOnly() {
  return <App />
}