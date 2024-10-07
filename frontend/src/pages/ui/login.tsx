import { Link } from 'react-router-dom'

import { LoginForm } from '@/features/user/login'
import { FlexCentred, TypographyH2, TypographyP } from '@/shared/ui'

const LoginPage = () => {
  return (
    <FlexCentred>
      <TypographyH2>Sign In</TypographyH2>
      <TypographyP muted>Happy to see you come back</TypographyP>
      <LoginForm />
      <TypographyP className="text-center mt-2" muted>
        Do not have an account yet?{' '}
        <Link className="text-primary" to="/register">
          Sign up
        </Link>
        .
      </TypographyP>
    </FlexCentred>
  )
}

export { LoginPage }
