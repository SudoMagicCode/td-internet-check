import socket


class connection:

    def __init__(self, ownerOp) -> None:
        self.ownerOp = ownerOp
        self.status_op = ownerOp.op('base_status')
        self._update_status(False)

    def _update_status(self, status: bool) -> None:
        self.status_op.par.Connected = status

    def Check_status(self) -> None:
        connection: bool = self._check_status(ip=self.ownerOp.par.Pollingip.eval(),
                                              port=self.ownerOp.par.Pollingport.eval())
        self._update_status(connection)

    def _check_status(self, ip: str, port: int) -> bool:
        a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            a.connect((ip, port))
            return True
        except socket.error:
            return False
