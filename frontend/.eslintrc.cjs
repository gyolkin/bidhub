module.exports = {
  root: true,
  env: { browser: true, es2020: true },
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended',
    'plugin:react-hooks/recommended',
    'plugin:react/recommended',
    'plugin:react/jsx-runtime',
    'prettier',
  ],
  ignorePatterns: ['dist', '.eslintrc.cjs'],
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
    project: ['./tsconfig.json', './tsconfig.node.json'],
    tsconfigRootDir: __dirname,
  },
  plugins: ['react-refresh', 'simple-import-sort'],
  rules: {
    'react-refresh/only-export-components': [
      'warn',
      { allowConstantExport: true },
    ],
    'react/prop-types': 'off',
    'simple-import-sort/imports': [
      'error',
      {
        groups: [
          ['^\\w'],
          ['^[@/]'],
          [
            '^@/app/(.*)$',
            '^@/processes/(.*)$',
            '^@/pages/(.*)$',
            '^@/widgets/(.*)$',
            '^@/features/(.*)$',
            '^@/entities/(.*)$',
            '^@/shared/(.*)$',
            '^@(.*)$',
          ],
          ['^[./]', '^[../]'],
        ],
      },
    ],
    'simple-import-sort/exports': 'error',
  },
}
