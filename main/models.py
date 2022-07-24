from django.db import models
from django.core import validators 
# Create your models here.
from datetime import date
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import now

class FirstDispute(models.Model):
    CHOICES=(
    ('1', '01 О заключении, изменении и расторжении договоров'),
    ('2', '02 О недействительности сделок'),
    ('3', '03 О неисполнении или ненадлежащем исполнении обязательств по договорам'),
    ('4', '04 Внедоговорные обязательства'),
    ('5', '05 О проверке законности ненормативных актов, действий (бездействий) государственных органов, должностных лиц'),
    ('6', '06 О признании права собственности'),
    ('7', '07 Об истребовании имущества из чужого незаконного владения (виндикационный иск)'),
    ('8', '08 О нарушении прав, не связанных с лишением владения (негаторный иск)'),
    ('9', '09 О признании не подлежащим исполнению исполнительного документа, по которому взыскание производится в бесспорном порядке'),
    ('10', '10 О взыскании налогов, сборов, экономических санкций, других обязательных платежей в бюджет'),
    ('11', '11 О возврате из бюджета и государственных внебюджетных фондов денежных средств, списанных в бесспорном порядке'),
    ('12', '12 О ликвидации юридических лиц'),
    ('13', '13 О привлечении к субсидиарной ответственности'),
    ('14', '14 О прекращении деятельности индивидуальных предпринимателей'),
    ('15', '15 Об экономической несостоятельности (банкротстве)'),
    ('16', '16 О защите деловой репутации'),
    ('17', '17 Об установлении фактов, имеющих юридическое значение'),
    ('18', '18'),
    ('19', '19 По жалобам на нотариальные действия или отказ в их совершении'),
    ('20', '20 Нарушение законодательства об охране окружающей среды'),
    ('21', '21 Учредительство'),
    ('22', '22 О понуждении совершить определённые действия'),
    ('23', '23 Иные категории'),
    ('24', '24 Обжалование ответов на обращения юридических лиц, индивидуальных предпринимателей или граждан'),
    ('25', '25 О продлении приостановления (запрета) деятельности по заявлениям контролирующих органов'),
    ('26', '26 О приостановлении деятельности по заявлениям контролирующих органов'),
    ('27', '27 Споры в отношении находящегося в государственной собственности имущества'),
    ('28', '28 По жалобам на действия судебного исполнителя'),
    ('29', '29 О возбуждении приказного производства '),
    ('30', '30 О взыскании денежных средств'),
    ('31', '31 О выдаче исполнительного документа'),
    ('32', '32 О выдаче исполнительного документа на принудительное исполнение медиативного соглашения'),
    ('33', '33 О признании и приведении в исполнение решений иностранных судов на территории Республики Беларусь'),
    )
    value = models.CharField("Категория спора (подкатегория 1):", max_length=122, choices=CHOICES, default=CHOICES[0][1])
    def __str__(self):
        return self.value 

def get_min_length():
        min_length = 10
        return min_length 

def get_min_length_case_number():
        min_length = 3
        return min_length 



class Card(models.Model): 
    INSTANCE_CHOICES = (
        ('Первая', 'Первая'), 
        ('Апеляционная', 'Апеляционная'), 
        ('Кассационная', 'Кассационная'), 
        ('Надзорная', 'Надзорная'),
    )
    PROCEEDING_CHOICES =(
        ('Административное', 'Административное'), 
        ('Интеллектуальное', 'Интеллектуальное'), 
        ('Экономическое', 'Экономическое'),
    )
    YES_OR_NO_CHOICES = (
        ('Есть', 'Есть'), 
        ('Нет', 'Нет'),
    )
    CHOICES = (
        ('None', ''),
        ("Нет", "Нет"), 
        ("Изменено", "Изм."), 
        ("Отказано", "Отк."),)

    REQUIREMENTS = (
        ('None', ''),
        ('Удовлетворено', 'Удовлетворено'), 
        ('Удовлетворено в части', 'Удовлетворено в части'), 
        ('Отказано', 'Отказано'), 
    )
    TRIALS = (("Верховный суд Республики Беларусь", "Верховный суд Ресублики Беларусь"), 
        ("Экономический суд Брестской области", "Экономический суд Брестской области"), 
        ("Экономический суд Витебской области", "Экономический суд Витебской области"), 
        ("Экономический суд Гомельской области", "Экономический суд Гомельской области"), 
        ("Экономический суд Гродненской области", "Экономический суд Гродненской области"), 
        ("Экономический суд города Минска", "Экономический суд города Минска"), 
        ("Экономический суд Минской области", "Экономический суд Минской области"), 
        ("Экономический суд Могилевской области", "Экономический суд Могилевской области"), 
    )
    SECOND1_DISPUTE = (
            ('None', 'Выбирается при значения "Подкатегория 1" - "01 О заключении, изменении и расторжении договоров"'),
            ('01.01 о понуждении к заключению договора', '01.01 о понуждении к заключению договора'), 
            ('01.02 о разногласиях по условиях договора', '01.02 о разногласиях по условиях договора'),
            ('01.03 об изменении условий договора', '01.03 об изменении условий договора'),
            ('01.04 о расторжении договора', '01.04 о расторжении договора'),
            ('01.05 о расторжении договора и выселении', '01.05 о расторжении договора и выселении'),
            ('01.06 о признании недействительным (неправомерным) одностороннего отказа от договора', '01.06 о признании недействительным (неправомерным) одностороннего отказа от договора'),
            ('01.07 о признании договора незаключённым', '01.07 о признании договора незаключённым'), 
            )

    SECOND2_DISPUTE = (
    ('None', 'Выбирается при значения "Подкатегория 1" - "02 О недействительности сделок"'),
    ('02.01 о признании сделки недействительной', '02.01 о признании сделки недействительной'), 
    ('02.02 о применении последствий недействительности сделки', '02.02 о применении последствий недействительности сделки'),
    ('02.03 о признании торгов недействительными', '02.03 о признании торгов недействительными'),
    ('02.04 об установлении факта ничтожности сделки', '02.04 об установлении факта ничтожности сделки'),
    ('02.05 о применении последствий ничтожности сделки', '02.05 о применении последствий ничтожности сделки'),
    )
    THIRD_DISPUTE = (
        ('None', 'Выбирается при значениях "Подкатегория 1" - "02 О недействительности сделок" и "Подкатегория 2" - "02.03 о признании торгов недействительными"'),
        ('02.03.01 о признании незаконными решения и (или) действия (бездействия) организации либо членов комиссии', '02.03.01 о признании незаконными решения и (или) действия (бездействия) организации либо членов комиссии'),
        ('02.03.02 иные споры о признании торгов недействительными', '02.03.02 иные споры о признании торгов недействительными'),
    )
    name = models.CharField("Наименование постановления" ,max_length=400, validators=[validators.MinLengthValidator(get_min_length, message="Для продолжения работы с формой необходимо ввести минимум 10 символов"),])
    date = models.DateField(default=now)
    case_number = models.CharField("Номер дела:", max_length=40, validators=[validators.MinLengthValidator(get_min_length_case_number, message="Для продолжения работы с формой необходимо ввести минимум 3 символа")])
    documents = models.URLField("Связанные документы (ссылки):", max_length=300, blank=True, null=True, validators=[validators.URLValidator(schemes=None,regex=None,message=None,code=None)])
    trial = models.CharField("Наименование суда", max_length=37, choices=TRIALS, default=TRIALS[0][1])
    instance = models.CharField("Инстанция:", max_length=12, choices=INSTANCE_CHOICES, default=INSTANCE_CHOICES[0][1])
    intial = models.CharField("Первоначальное решение первой инстанции", choices=REQUIREMENTS, blank=True, null=True, max_length=200)
    counter = models.CharField("Встречное решение первой инстанции", choices=REQUIREMENTS,blank=True, null=True, max_length=200)
    appellate = models.CharField("Решение апелляционной инстанции", choices=CHOICES, blank=True, null=True, max_length=200)
    cassation = models.CharField("Решение кассационной инстанции", choices=CHOICES,blank=True, null=True, max_length=200)
    proceeding = models.CharField("Вид судопроизводства:", max_length=16, choices=PROCEEDING_CHOICES, default=PROCEEDING_CHOICES[0][1])
    first_dispute = models.ManyToManyField(FirstDispute) 
    second1_dispute = models.CharField("Категория спора (подкатегория 2-1)", max_length=122, choices=SECOND1_DISPUTE, blank=True, null=True)
    second2_dispute = models.CharField("Категория спора (подкатегория 2-2)", max_length=122, choices=SECOND2_DISPUTE, blank=True, null=True)
    third_dispute = models.CharField("Категория спора (подкатегория 3)", max_length=122, choices=THIRD_DISPUTE, blank=True, null=True)
    motivation = models.CharField("Наличие мотивировочное части:", max_length=4, choices=YES_OR_NO_CHOICES, blank=True, null=True)
    review = models.CharField("История рассмотрения:", max_length=4, choices=YES_OR_NO_CHOICES, blank=True, null=True)
    original_claim = models.CharField("Первоначальное требование:", max_length=300, default="Не значится")
    counter_claim = models.CharField("Встречное требование:", max_length=300, default="Не значится")
    description = models.TextField("Полное постановление",  default='Полное постановление отсутствует.')
    upload = models.FileField(upload_to="uploads/%Y/%m/%d/", blank=True, null=True)
    class Meta:
        ordering = ["-date"]
    def __str__(self):
        return self.name 
    

