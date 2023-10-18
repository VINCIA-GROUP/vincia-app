enum AplicationErrors {
  internalError(
      code: "0",
      message: "Houve um erro no aplicativo. Tente novamente mais tarde."),
  unauthorizedAccess(
      code: "1000",
      message: "Você não tem autorizatição para efetuar essa função.");

  const AplicationErrors({required this.code, required this.message});

  final String code;
  final String message;
}
