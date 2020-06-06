class State(models.Model):
    STATES = (
        (0, 'OK'),
        (1, 'WARNING'),
        (2, 'ERROR'),
        (3, 'FAILURE'),
    )

    state = models.IntegerField(choices=STATES, verbose_name='состояние')
    logs = models.TextField(verbose_name='журнал')

    def get_state(self):
        return self.get_state_display()

    def __str__(self):
        return f'{self.get_state()}'

    class Meta:
        verbose_name = 'состояние'
        verbose_name_plural = 'состояния'
