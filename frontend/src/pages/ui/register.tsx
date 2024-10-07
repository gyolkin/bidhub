import { Link } from 'react-router-dom'

import { RegisterForm } from '@/features/user/register'
import { FlexCentred, TypographyH2, TypographyP } from '@/shared/ui'

const RegisterPage = () => {
  return (
    <FlexCentred>
      <TypographyH2>Sign Up</TypographyH2>
      <TypographyP muted>Join our community right now</TypographyP>
      <RegisterForm />
      <TypographyP className="text-center mt-2" muted>
        Already have an account?{' '}
        <Link className="text-primary" to="/login">
          Sign in
        </Link>
        .
      </TypographyP>
    </FlexCentred>
  )
}

export { RegisterPage }
